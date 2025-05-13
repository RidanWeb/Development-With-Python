from ride import Ride, RideRequest, RideMatching, RideSharing
from user import Rider, Driver
from vehicle import Vehicle, Car, Bike


coloJai = RideSharing("CloJai")

ridan = Rider("Ridan", "j@gmail.com", "123456789", "Dhaka", 1000)
kabir = Rider("kabir", "k@gmail.com", "123456789", "Sylhet", 500)
coloJai.addRider(ridan)
coloJai.addRider(kabir)


foisal = Driver("Faisal", "f@gmail.com", "987654321", "Dhaka")
hasan = Driver("Hasan", "h@gmail.com", "98754321", "Dhaka")
coloJai.addDriver(foisal)
coloJai.addDriver(hasan)

ridan.requestRide(coloJai, "Chittagong", "car")
foisal.reachDestination(ridan.currentRide)

ridan.showCurrentRide()


# print(coloJai)