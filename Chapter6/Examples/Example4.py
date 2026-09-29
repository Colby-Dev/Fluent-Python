class HauntedBus: 
    """ A bus Model haunted by ghost passengers """

    def __init__(self, passengers=[]): 
        self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


if __name__ == "__main__": 

    bus1 = HauntedBus(["Alice", "Cooper", "Mac"])
    print(bus1.passengers)
    bus1.pick("Sarah")
    bus1.drop("Alice") 

    bus2 = HauntedBus()
    bus2.pick("Test")
    print(bus2.passengers is bus1.passengers)
    
    bus3 = HauntedBus()
    print(f'{bus3.passengers} <--- HOW?!')

    

