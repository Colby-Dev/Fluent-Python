#normal class
class DemoPlainClass:
    a: int
    b: float = 1.1
    c = 'spam'

#Named Tuple class
import typing
class DemoNTClass(typing.NamedTuple):
    a: int
    b: float = 1.1
    c = 'spam'

#Dataclass type
from dataclasses import dataclass
@dataclass
class DemoDataClass():
    a: int 
    b: float = 1.1
    c = 'spam'

if __name__ == '__main__':
    print(f'This is a normal class instance annotations {DemoPlainClass().__annotations__} and the values {DemoPlainClass().b}, {DemoPlainClass().c}\n')

    print(f'This is a NamedTuple class instance which looks similar but uses collections as the attributes: {DemoNTClass.b}, {DemoNTClass.c}\n')

    print(f'This is a Dataclass instance which acts different from a NamedTuple. {DemoDataClass.b} , {DemoDataClass.c} the annotations are {DemoDataClass.__annotations__}')



