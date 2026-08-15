from collections import namedtuple
import json

city = namedtuple('city','name country population coordinates')

def namedTuples(): 
    place = city('SLC', 'USA', 5.3, (100, 200))
    print(place)
    print(f' {place.name} \n {place.country} \n {place.population} \n {place.coordinates}')

    # Using the ._fields, ._make, and ._asdict methods
    print(place._fields)
    Coordinate = namedtuple('Coordinate', 'lat lon')
    delhi_data = ('Delhi NCR', 'IN' , 21.935, Coordinate(28.61, 77.20))
    delhi = city._make(delhi_data)
    delhidict = delhi._asdict()
    print(delhidict)

    jdelhidata = json.dumps(delhidict)
    print(jdelhidata)



if __name__ == '__main__': 
    namedTuples()

