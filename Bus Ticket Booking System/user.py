from bus import Bus, BusSystem


class Passenger:
    def __init__(self, name, phone, bus):

        self.name = name
        self.phone = phone
        self.bus = bus


    def bookTicket(self, busNumber, name, phone, seat):
        bus = BusSystem()
        bus.bookTicket(busNumber, name, phone, seat)
        
        print(f"Ticket booked successfully for {name} on bus {busNumber}.")

    def viewBus(self):
        bus = BusSystem()
        bus.viewBuses()



class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def login(self, username, password):

        if username == "admin" and password == 1234:

            return True

        else:
            return False



    def add_bus(self, number, route, seat):
        bus = Bus(number, route, seat)

        bus_system = BusSystem()
        bus_system.addBus(bus)
        print(f"Bus {number} added successfully.")


    def viewBuses(self):
        bus_system = BusSystem()
        bus_system.viewBuses()