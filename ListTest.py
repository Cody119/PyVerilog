from numba import njit, double, typeof, deferred_type
from numba.experimental import jitclass
from numba.typed import List

@njit(double(double))
def addOne(x):
    return x + 1.0

@njit(double(double))
def addTwo(x):
    return x + 2.0

MyFun = double(double).as_type();
MyList = typeof(List.empty_list(MyFun))
print(MyList)

@njit(MyList(MyList, MyFun))
def magic(l, f):
    l.append(f)
    return l

x = List.empty_list(MyFun)
y = magic(x, addOne)
l = magic(y, addTwo)

@njit(double(MyList))
def test(x):
    return x[0](3.0)
@njit(double(MyList))
def test2(x):
    return x[1](3.0)

print(test(x), test2(x))