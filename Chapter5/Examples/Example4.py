from dataclasses import dataclass, field

@dataclass
class Clubmember: 
    name: str
    guests: list = field(default_factory=list)
    ages: list[int] = field(default_factory=list)
    athlete: bool = field(default_factory=list, repr=False)

if __name__ == '__main__':
    test = Clubmember(name="test")
    test.guests.append("test 1")
    print(test.name, test.guests)
    print(type(test.guests))
