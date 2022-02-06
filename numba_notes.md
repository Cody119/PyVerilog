# Current limitations

Numba is still pretty limited, some points of note are as follows:
 1. Any form of useful closure cannot be used (the only excpection is if a 
    closure function is exclusivley used in the function)
 2. Methods are a bit wierd, `MyClass.my_instance_method` wont work as the type
    dict for the generated jit class only has static methods. And due to 1,
    `x = my_class_instance.my_instance_method` also wont work
 3. Need to use `numba.typed.List` and `numba.typed.Dict` for lists and dicts
 4. `yield` works apparently? Never tested and defenitly `send` dosent



The Plan
Transpiler Example:
```verilog
module FlipFlop(input clk, input i, output reg o);
    always @(posedge clk)
        o <= i;

module Test(input clk, input x, output y);
    wire fo;
    reg r1;
    assign y = r1;

    FlipFlop(.clk(clk), .i(x), .o(fo));

    always @(posedge clk)
        r1 <= fo;

endmodule
```

```python
FlipFlop_builder = ModuleBuilder()

@FlipFlop_builder.c
class FlipFlop:
    i: InputWire # [0:0]
    o: OutputReg # [0:0]


```