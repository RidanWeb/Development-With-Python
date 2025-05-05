from manu import Manu
from restaurant import Restaurant
from orders import Order
from users import Admin, Employee, Customer
from foodItems import FoodItem




restaurant = Restaurant("Food Palace")

def cust_manu():

    name = input("Enter your name: ")
    phone = int(input("Enter your phone number: "))
    email = input("Enter your email: ")
    address = input("Enter your address: ")

    customer = Customer(name = name, phone = phone, email = email, address = address)

    while True:

        print(f"Welcome {customer.name} !!!")

        print("1. View Menu")
        print("2. Add Item to Cart")
        print("3. View Cart")
        print("4. Pay Bill")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:

            customer.view_menu(restaurant)

        elif choice == 2:

            item_name = input("Enter the name of the item: ")
            quantity = int(input("Enter the quantity: "))
            customer.add_to_cart(restaurant, item_name, quantity)

        elif choice == 3:  

            customer.view_cart()

        elif choice == 4:

            customer.pay_bill()

        elif choice == 5:

            print("Exiting...")
            break   

        else:   
            print("Invalid choice. Please try again.")















def admin_manu():

    name = input("Enter your name: ")
    phone = int(input("Enter your phone number: "))
    email = input("Enter your email: ")
    address = input("Enter your address: ")

    admin = Admin(name = name, phone = phone, email = email, address = address)

    while True:

        print(f"Welcome {admin.name} !!!")

        print("1. Add new Item to Menu")
        print("2. Add new Employee")
        print("3. View Items in Menu")
        print("4. view Employees")
        print("5. Remove Item from Menu")
        print("6. Exit")
        
        choice = int(input("Enter your choice: "))

        if choice == 1:

            name = input("Enter the name of the item: ")
            price = float(input("Enter the price of the item: "))
            quantity = int(input("Enter the quantity of the item: "))

            item = FoodItem(name, price, quantity)

            admin.add_item(restaurant, item)

        elif choice == 2:

            name = input("Enter the name of the employee: ")
            phone = int(input("Enter the phone number of the employee: "))
            email = input("Enter the email of the employee: ")
            address = input("Enter the address of the employee: ")
            age = int(input("Enter the age of the employee: "))
            degination = input("Enter the degination of the employee: ")
            salary = float(input("Enter the salary of the employee: "))

            emp = Employee(name = name, phone = phone, email = email, address = address, age = age, degination = degination, salary = salary)

            admin.add_employee(restaurant, emp)

        elif choice == 3:  

            admin.view_items(restaurant)

        elif choice == 4:

            admin.view_employees(restaurant)

        elif choice == 5:

            item_name = input("Enter the name of the item to remove: ")

            admin.remove_item(restaurant, item_name)

        elif choice == 6:

            print("Exiting...")
            break

        else:   
            print("Invalid choice. Please try again.")




while True:
    print("Welcome to the Restaurant Management System")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        cust_manu()

    elif choice == 2:

        admin_manu()

    elif choice == 3:

        print("Exiting...")
        break

    else:   
        print("Invalid choice. Please try again.")
