from user import Admin, Passenger
from bus import Bus



bus = Bus(2546, "Dhaka to Chittagong", 50)



print("Welcome to the Bus Ticket Booking System")
print("1. Admin Login")
print("2. Book Ticket")
print("3. View Buses")
print("4. Exit")


choice = int(input("Enter your choice: "))

while choice != 4:

    if choice == 1:

        username = input("Enter username: ")
        password = int(input("Enter password: "))
        admin = Admin(username, password)
        

        if admin.login(username, password):

            print("1. Add Bus")
            print("2. View All Buses")
            print("3. Exit")
            adminChoice = int(input("Enter your choice: "))


            if adminChoice == 1:

                busNumber = int(input("Enter bus number: "))
                route = input("Enter bus route: ")
                totalSeats = int(input("Enter total seats: "))
                
                admin.addBus(busNumber, route, totalSeats)

            elif adminChoice == 2:
                
                admin.viewBuses()

            elif adminChoice == 3:

                print("Exiting...")
                break

        


        else:
            print("Invalid username or password.")
            choice = int(input("Enter your choice: "))
            continue
            
        
    elif choice == 2:

        busNumber = input("Enter bus number: ")
        name = input("Enter passenger name: ")
        phone = input("Enter passenger phone number: ")
        seat = int(input("Enter number of seats to book: "))
        
        passenger = Passenger(name, phone, bus)

        passenger.bookTicket(busNumber, name, phone, seat)

    
    elif choice == 3:
        
        bus.viewBuses()