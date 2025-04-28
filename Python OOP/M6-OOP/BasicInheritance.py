# Bus Company

class Company:
    def __init__ (self, name, address):
        self.name = name
        self.address = address
        self.buses = []
        self.drivers = []
        self.routes = []
        self.passengers = []
        self.tickets = []
        self.employees = []
        self.managers = []



class Drivers:
    def __init__ (self, name, license, phone, age) -> None: 
        self.name = name
        self.license = license
        self.phone = phone
        self.age = age



class Counter:
    def __init__ (self):
        
        def PurchaseATicket(self, start, destination, time):
            # Logic to purchase a ticket
            pass


class Passengers:
    def __init__ (self, name, phone):
        self.name = name
        self.phone = phone





# Example of Inheritance ===================

class Gadget:
    def __init__ (self, name, color, price) -> None:
        self.name = name
        self.color = color
        self.price = price

    def run(self):
        print(f"{self.name} is running")



class Phone(Gadget):
    def __init__ (self, name, color, price, camera) -> None:
        super().__init__(name, color, price)
        self.camera = camera



myPhone = Phone("Samsung", "Red", 25000, "250MP")

print(myPhone.name)
print(myPhone.color)
myPhone.run()