import typing

class City(typing.NamedTuple):
    continent: str
    name: str
    country: str
    
cities =[
        City('NA', 'SLC', 'USA'),
        City('NA', 'SATX', 'USA'),
        City('EU', 'BRLN', 'DEU')]

def match_DEU():
    results = []
    for city in cities: 
        match city:
            case City(country='DEU'):
                results.append(city)
    return print(f'Match sucessful for {results[0].name}, located in the {results[0].continent}.')

if __name__ == '__main__':

    match_DEU()
