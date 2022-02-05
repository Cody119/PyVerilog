from numba import njit, double, typeof, deferred_type
from numba.experimental import jitclass
from numba.typed import List

### Class Test

# test_type = deferred_type()
# MyFun = double(test_type).as_type();
# MyList = typeof(List.empty_list(MyFun))


# specs = [("test2", MyList)]
# @jitclass(specs)
# class Test:

#     def __init__(self, x):
#         self.test2 = x

#     def get(self):
#         return self.test2

#     def testt(self, x):
#         print(self.test2[0](self))
#         return self.test2[0](x)

# test_type.define(Test.class_type.instance_type)

# @njit(double(test_type))
# def test(x):
#     print(x)
#     return 3.0

# @njit #(MyList(MyList, MyFun))
# def magic(l, f):
#     l.append(f)
#     return l

# l = List.empty_list(MyFun)
# x = Test(l)
# print(x)
# magic(l, test)
# magic(x.test2, test)
# x.testt(x)


