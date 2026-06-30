from abc import ABC,abstractmethod

class Vehicle(ABC):
    def __init__(self,n):
        self.number_of_tyre=n
    @abstractmethod
    def start(self):
        pass


class Bike(Vehicle):
    def __init__(self, n):
        self.number_of_tyre=n
    def start(self):
        print("start with Kick")

class Scooty(Vehicle):
    def __init__(self, n):
        self.number_of_tyre=n
    def start(self):
        print("Self Start")

class Car(Vehicle):
    def __init__(self, n):
        self.number_of_tyre=n
    def start(self):
        print("Start with Key")


c1=Car(4)

c1.start()
    


