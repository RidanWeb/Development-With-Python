

class Bus:
    
    
    def __init__(self, number, route, totalSeats):
        self.number = number
        self.route = route
        self.totalSeats = totalSeats
        self.seatFare = 500
        self.bookedSeat = 0


    @staticmethod
    def bookSeat(self, seat):

        if self.bookedSeat + seat <= self.totalSeats:
            self.bookedSeat += seat
            print(f"Successfully booked {seat} seats on bus {self.number} for {self.seatFare * seat} taka.")
        else:
            print("Not enough seats available.")


class BusSystem:
    def __init__(self):
        self.busesList = []
        self.passengerList = []


    def addBus(self, bus):
        self.busesList.append(bus)
        print(f"Bus {bus.number} added to the system.")

    def viewBuses(self):
        if not self.busesList:
            print("No buses available.")
        else:
            print("Available Buses:")
            for bus in self.busesList:
                print(f"Bus Number: {bus.number}, Route: {bus.route}, Total Seats: {bus.totalSeats}, Booked Seats: {bus.bookedSeat}")

    
    def findBus(self, busNumber):
        for bus in self.busesList:
            if bus.number == busNumber:
                return bus
        return None
    
    def seatAvailable(self, busNumber):
        bus = self.findBus(busNumber)
        if bus:
            availableSeats = bus.totalSeats - bus.bookedSeat
            return availableSeats
        else:
            return 0


    def bookTicket(self, busNumber, seat):

        bus = self.findBus(busNumber)
        if bus:
            if self.seatAvailable(busNumber) >= seat:
                bus.bookSeat(bus, seat)


    

    

    
