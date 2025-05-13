from abc import ABC


class Vehicle(ABC):

    speed = {

        'car' : 50,
        'bike' : 30,
        'cng' : 20
    }

    def __init__(self, vehicleType, vehicleLicrnse, rate) -> None:
        self.vehicleType = vehicleType
        self.vehicleLicrnse = vehicleLicrnse
        self.rate = rate


class Car(Vehicle):

    def __init__(self, vehicleType, vehicleLicrnse, rate) -> None:
        super().__init__(vehicleType, vehicleLicrnse, rate)



class Bike(Vehicle):

    def __init__(self, vehicleType, vehicleLicrnse, rate) -> None:
        super().__init__(vehicleType, vehicleLicrnse, rate)