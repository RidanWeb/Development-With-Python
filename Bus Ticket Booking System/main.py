from user import Admin
from bus import BusSystem, Bus


busSystem = BusSystem()


def adminManu():

    username = input("Enter username: ")
    password = int(input("Enter password: "))
    admin = Admin(username, password)

    if admin.login(username, password):

        while True:

            print("1. Add Bus")
            print("2. View All Buses")
            print("3. Exit")
            adminChoice = int(input("Enter your choice: "))

            if adminChoice == 1:
                busNumber = int(input("Enter bus number: "))
                route = input("Enter bus route: ")
                totalSeats = int(input("Enter total seats: "))
                
                bus = Bus(busNumber, route, totalSeats)

                admin.addBus(busSystem, bus)
            
            elif adminChoice == 2:
                admin.viewBuses()

            elif adminChoice == 3:
                return
        
        


    else:
        print("Invalid username or password.")
        return
    





while True:


    print("Welcome to the Bus Ticket Booking System")

    print("1. Admin Login")
    print("2. Book Ticket")
    print("3. View Buses")
    print("4. Exit")


    choice = int(input("Enter your choice: "))


    if choice == 1:

        adminManu()

    elif choice == 2:

        busNumber = input("Enter bus number: ")
        seat = int(input("Enter number of seats to book: "))

        busSystem.bookTicket(busNumber, seat)

    elif choice == 3:

        busSystem.viewBuses()


