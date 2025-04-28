# Base Class or Parent Class 

class Vehicle:
    def __init__ (self, name, price) -> None:
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Bus Name: {self.name}, Price: {self.price}"


class Bus(Vehicle):
    def __init__ (self, name, price, seat) -> None:

        self.seat = seat
        super().__init__(name, price)

        def __repr__(self) -> str:
            print(f'Seat: {self.seat}')
            return super().__repr__()
        


class Truck(Vehicle):
    def __init__ (self, name, price, capacity) -> None:

        self.capacity = capacity
        super().__init__(name, price)


class ACBus(Bus):

    def __init__ (self, name, price, seat, temperature) -> None:
        self.temperature = temperature
        super().__init__(name, price, seat)

    def __repr__(self):

        print(f"Temperature is {self.temperature}")
        return super().__repr__()
    


MyACBus = ACBus("Green Line", 100000000, 25, 18)

print(MyACBus)

