# Notes on simulating Verilog

## Basic Scheduling 
At any given time, a particular always block can only apear in the execution list of a particular simulation time
once (for the purposes of this rule, an always block remains in the list until it has completed execution). 
For example, if we have the following code:
```verilog
module ChangeTest;
    reg x = 0;

    always @(x) begin $display("Block 1 ", x); x=0; end
    always @(x) begin $display("Block 2 ", x); x=0; end

    initial begin
        x = 1;
        #1; // let events resolve
        $finish;
    end 
endmodule
```
When x changes in the initial b, both Block 1 and Block 2 are scheduled for execution in the current simulation time. 
We will assume Block 1 runs first (wether or not this is true is undefined, the standards state either order is valid).
There are 2 things to note here. First, Block 2 will only run once even though, before it has had a chance to run, x has
changed twice. As it is already scheduled to run in this simulation time, it will not be added again. Similarly Block 1 will
only run once, as it "remains on the schedule" until it has been complete, and therefore will not be scheduled again in this
time step.

It is worth also considering this slightly modified version:
```verilog
module ChangeTest;
    reg x = 0;

    always @(x) begin $display("Block 1 ", x); x=0; end
    always @(posedge x) begin $display("Block 2 ", x); x=0; end

    initial begin
        x = 1;
        #1; // let events resolve
        $finish;
    end 
endmodule
```
Again assuming that Block 1 runs first, the result will be the same. Even though x is 0 by the time Block 2 runs, the
posedge trigger has already caused Block 2 to be added to the schedule. I do not believe there is anyway to remove something from
the schedule once it has been added.

## Non-Blocking
(This one could probably use a few more experiments)
Consider the following code:
```verilog
module NonBlockTest;
    reg x = 0;
    reg z = 0;

    initial begin
        x = 1;
        #5 $finish;
    end
    
    always @(x) begin $display("B1: X is ", x,z,, $time); x <= !x; z <= !z; end
    always @(x) begin $display("B2: X is ", x,z,, $time); x <= !x; z <= !z; end
endmodule
```
THis will cause an infinite loop. $time will remain 1 for the duration and 
the output will be:
```
B1: X is 10           0
B2: X is 10           0
B2: X is 01           0
B1: X is 01           0
```
repeated forever (B1 and B2 on lines 1 and 2 can appear in either order, lines 3 and 4 will behave similarly).
The order of events roughly follows the following:
 1. x changes in the initial block, this causes B1 and B2 to be scheduled for this simulation time.
 2. B1 (or B2) is run, x and z are not changed, they are instead added to a list of non blocking changes for this
    simulation time.
 3. B2 (or B1) is run, x and z changes it wants to make are identical to what is already listed (but if they were different
    they would overwrite the excising ones, last non-blocking run is the one that takes effect)
 4. The schedule for this simulation time is now empty, ALL non-blocking values are resolved. THe value changes
    cause B1 and B2 to scheduled again for this simulation time.
 5. repeat step 2 to 5. (Note that time never advances)

# TODO 
run same always block twice, but it branches differently such that it causes modifications to the same variable
but with different delays

Trigger this always block twice in same time step (might be impossible?)
```verilog
always @(x) if (z) 
    #4 y <= 1; 
else
    #5 y <= 1;
```


(Code used to figure all this shit out)
```verilog
module jdoodle;
    reg x = 0;
    
    // always @(posedge x, negedge x) begin $display("1 posedge ", x); x = 0; end
    always @(posedge x, negedge x) begin $display("2 posedge ", x); x = 0; end

    initial begin
        $display ("Welcome to JDoodle!!!");
        x = 1;
        // x = 0;
        $display("1 inital ", x);
        #1;
        $display("2 inital ", x);
        x = 1;
        $display("3 inital ", x);
        #5 $finish;
    end
    
    always @(x) begin $display("X is ", x); x = !x; end
    //always @(x) begin $display("X is ", x); x = !x; end
endmodule
```