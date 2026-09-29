import copy as cp
class Bus:
    def __init__(self, passengers=None):
        if passengers is None: 
            self.passengers = []
        else: 
            self.passengers = list(passengers)

    def pick(self, name): 
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)

if __name__ == "__main__":

    bus1 = Bus(['Alice', 'Cooper', 'Jaxson'])
    bus2 = cp.copy(bus1)
    bus3 = cp.deepcopy(bus1)
    print(bus1.passengers, bus2.passengers)
    print(bus1.passengers == bus2.passengers)
    print(id(bus1.passengers), id(bus2.passengers))
