from collections import namedtuple
import typing
from dataclasses import dataclass

# Using named tuple: 
def named_tuple():
    Coordinate = namedtuple('Coordinate', 'lat lon')
    print(issubclass(Coordinate, tuple))
    moscow = Coordinate(lat = 55.756, lon = 37.617)
    print(moscow.lat == 55.756)

# Using typing library:
def typing_tuple():
    Coordinate = typing.NamedTuple('Coordinate',
                                   [('lat', float), ('lon',float)])
    print(issubclass(Coordinate, tuple))
    print(typing.get_type_hints(Coordinate))
    print(Coordinate._fields)

# Using Dataclasses
@dataclass(frozen=True)
class Coordinate:
    lat: float
    long: float

    def __str__(self):
        ns = 'N' if self.lat >= 0 else 'S'
        we = 'E' if self.long >= 0 else 'W'
        return f'{abs(self.lat):.1f} {ns}, {abs(self.long):.1f} {we}'

if __name__ == '__main__': 
    named_tuple()
    typing_tuple()
    cords = Coordinate(lat = 24, long = 32.1234)
    print(cords)
