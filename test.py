from typing import Type, Union

class MyTest:
    def __getitem__(self, x: int) -> Union[Type[int], Type[str]]:
        return int if x==0 else str
Y=MyTest()

class Test2:
    x: Y[0]

    