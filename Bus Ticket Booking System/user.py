# from bus import Bus, BusSystem


class Passenger:
    def __init__(self, name, phone, bus):

        self.name = name
        self.phone = phone
        self.bus = bus


    def bookTicket(self,busSystem, busNumber, name, phone, seat):
        busSystem.bookTicket(busNumber, seat)
        
        # print(f"Ticket booked successfully for {name} phone {phone} on bus {busNumber}.")

    def viewBus(self, busSystem):
        busSystem.viewBuses()



class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def login(self, username, password):

        if username == "admin" and password == 1234:

            return True

        else:
            return False



    def addBus(self, busSystem, bus):

        busSystem.addBus(bus)

        print(f"Bus added successfully.")


    def viewBuses(self, busSystem):
        busSystem.viewBuses()