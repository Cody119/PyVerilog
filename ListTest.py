from numba import njit, double, typeof, int32, types
from numba.experimental import jitclass
from numba.typed import List, Dict

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


@jitclass
class Test:
    test: int

    def __init__(self):
        self.test = 1

    @staticmethod
    def test2(self) -> int:
        return self.test

@njit
def test2(self) -> int:
    return self.test

m = int32(Test.class_type.instance_type)
@njit(int32(m.as_type(), Test.class_type.instance_type))
def t(r, x):
    return r(x)

print(Test.test2)
# print(test2)
print(t(Test.test2, Test()))

d = Dict.empty(
    key_type=types.unicode_type,
    value_type=m.as_type(),
)

d["test"] = Test.test2

@njit
def aaa(r, x):
    return r["test"](x)

print("a")
print(aaa(d, Test()))