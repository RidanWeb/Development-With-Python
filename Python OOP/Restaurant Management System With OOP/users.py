from abc import ABC
from orders import Order

class User(ABC):

    def __init__(self, name, phone, email, address):

        self.name = name
        self.phone = phone
        self.email = email
        self.address = address


class Customer(User):

    def __init__(self, name, phone, email, address):

        super().__init__(name, phone, email, address)
        self.card = Order()

    def view_menu(self, restaurant):
            
        print(f"Menu for {restaurant.name}:")
        restaurant.manu.view_items()

    def add_to_cart(self, restaurant, item_name, quantity):

        item = restaurant.manu.find_item(item_name)

        if item:
            if quantity > item.quantity:
                print(f"Not enough quantity available for {item.name}.")    
            else:
                item.quantity = quantity
                self.card.add_item(item)
                print(f"Item {item.name} added to the cart.")

        else:
            print(f"Item {item_name} not found in the menu.")
        

    def view_cart(self):

        print(f"Card for {self.name}:")
        print("name\tPrice\tQuantity")

        for item, quantity in self.card.items.items():

            print("name\tPrice\tQuantity")
            print(f"{item.name}\t{item.price}\t{quantity}")

        print(f"Total Price: {self.card.total_price}")


    def pay_bill(self):

        print(f"Total Price: {self.card.total_price} Paid Successfully")
        self.card.clear_cart()




#Admin class is a subclass of User class and inherits its properties and methods.
class Admin(User):

    def __init__(self, name, phone, email, address):

        super().__init__(name, phone, email, address)


    def add_employee(self, restaurant, employee):

        restaurant.add_employee(employee)

    def view_employees(self, restaurant):

        restaurant.view_employees()

    def add_item(self, restaurant, item):

        restaurant.manu.add_item(item)

    def remove_item(self, restaurant, item_name):

        restaurant.manu.remove_item(item_name)

    def view_items(self, restaurant):

        restaurant.manu.view_items()



#Employee class is not used in the code but it is defined for future use.
class Employee(User):

    def __init__(self, name, phone, email, address, age, degination, salary):

        super().__init__(name, phone, email, address)
        self.age = age
        self.degination = degination
        self.salary = salary





 



















