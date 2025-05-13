from datetime import datetime
from vehicle import Vehicle, Car, Bike


class RideSharing:

    def __init__(self, companyName) -> None:

        self.companyName = companyName
        self.drivers = []
        self.riders = []
        self.rides = []

    def addRider(self, rider):
            self.riders.append(rider)

    def addDriver(self, driver):
            self.drivers.append(driver)

    def __str__(self):
           return f"RideSharing System: {self.companyName}. Drivers: {len(self.drivers)}. Riders: {len(self.riders)}. Rides: {len(self.rides)}"




class Ride:

    def __init__(self, startLocation, endLocation, vehicle)->None:

        self.startLocation = startLocation
        self.endLocation = endLocation
        self.driver = None
        self.rider = None
        self.startTime = None
        self.endTime = None
        self.estimatedFare = self.calculateFair(vehicle.vehicleType)
        self.vehicle = vehicle

    
    def assignDriver(self, driver):
        self.driver = driver
        print(f"Driver {driver.name} assigned to the ride.")

    def startRide(self):
        self.startTime = datetime.now()

    def endRide(self):
        self.endTime = datetime.now()
        self.rider.wallet -= self.estimatedFare
        self.driver.wallet += self.estimatedFare

    def calculateFair(self, vehicleType):
        distance =10
        fairPerKm = {
            'car' : 10,
            'bike' : 5,
            'cng' : 7
        }

        # return fairPerKm[vehicleType] * distance
        return distance * fairPerKm.get(vehicleType)

    def __repr__(self):
        return f"Ride from {self.startLocation} to {self.endLocation} with driver {self.driver.name}."
    



class RideRequest:

    def __init__(self, rider, endLocation):
        self.rider = rider
        self.endLocation = endLocation



class RideMatching:

    def __init__(self, drivers)->None:
        self.availableDrivers = drivers

    
    def findDriver(self, rideRequest, vehicleType):

        if len(self.availableDrivers) > 0:
            print("Looking for available drivers...")
            drivers = self.availableDrivers[0]

            if(vehicleType == "car"):
                vehicle = Car("car", "ABC123", 100)
            elif(vehicleType == "bike"):
                vehicle = Bike("bike", "XYZ456", 50)

            ride = Ride(rideRequest.rider.currentLocation, rideRequest.endLocation, vehicle)
            drivers.acceptRide(ride)



            return ride
    
    


