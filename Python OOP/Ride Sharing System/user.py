from abc import ABC, abstractmethod
from ride import RideRequest, RideMatching


class User(ABC):

    def __init__(self, name, email, nid) -> None:

        self.name = name
        self.email = email
        self.nid = nid

    @abstractmethod
    def displayProfile(self):
        raise NotImplementedError("Subclasses must implement this method")
    


class Rider(User):

    def __init__(self, name, email, nid, currentLocation, initialAmount):

        super().__init__(name, email, nid)
        self.currentLocation = currentLocation
        self.wallet = initialAmount
        self.currentRide = None

    def displayProfile(self):
        print(f"Rider Profile:\nName: {self.name}\nEmail: {self.email}\nNID: {self.nid}\nCurrent Location: {self.currentLocation}\nWallet Amount: {self.wallet}")

    def loadCash(self, amount):

        if amount > 0:
            self.wallet += amount
            print(f"Successfully loaded {amount} to wallet. New balance: {self.wallet}")
        
        else:
            print("Invalid amount. Please enter a positive value.")

    def updateLocation(self, newLocation):
        self.currentLocation = newLocation
        print(f"Location updated to: {self.currentLocation}")

    
    def requestRide(self, rideSharing, destination, vehicleType):

        rideRequest = RideRequest(self, destination)
        rideMatching = RideMatching(rideSharing.drivers)
        ride = rideMatching.findDriver(rideRequest, vehicleType)
        ride.rider = self
        self.currentRide = ride
        print("Yeah!! We get Ride...")


    def showCurrentRide(self):
        print("Current Ride Details:")
        print(f"Rider : {self.name}" )
        print(f"Start Location: {self.currentRide.startLocation}")
        print(f"End Location: {self.currentRide.endLocation}")
        print(f"Vehicle Type: {self.currentRide.vehicle.vehicleType}")
        print(f"Driver Name: {self.currentRide.driver.name}")
        print(f"Estimated Fare: {self.currentRide.estimatedFare}")
        print(f"Start Time: {self.currentRide.startTime}")
        print(f"End Time: {self.currentRide.endTime}")

    



class Driver(User):

    def __init__(self, name, email, nid, currentLocation)->None:


        super().__init__(name, email, nid)
        self.currentLocation = currentLocation
        self.wallet = 0


    def displayProfile(self):
        print(f"Driver Profile:\nName: {self.name}\nEmail: {self.email}\nNID: {self.nid}\nCurrent Location: {self.currentLocation}\nWallet Amount: {self.wallet}")

    def acceptRide(self, ride):
        ride.startRide()
        ride.assignDriver(self)

    def reachDestination(self, ride):
        ride.endRide()





