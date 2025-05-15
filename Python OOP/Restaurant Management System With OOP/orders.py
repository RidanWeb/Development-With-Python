
class Order:

    def __init__(self)->None:
        self.items = {}
        

    def add_item(self, item):

        if item in self.items:
            self.items[item] += item.quantity #Output: {<Item Apple>: 5, <Item Banana>: 2}

        else:
            self.items[item] = item.quantity

    def remve_item(self, item):

        if item in self.items:
            del self.items[item]

    @property
    def total_price(self):
        return sum(item.price * quantity for item, quantity in self.items.items())


    def clear_cart(self):
        self.items = {}
    


    def view_menu(self, restaurant):

        restaurant.manu.view_items()

    def order_item(self, restaurant, item_name):

        item = restaurant.manu.find_item(item_name)

        if item:
            print(f"Order placed for {item.name}.")
        else:
            print(f"Item {item_name} not found in the menu.")


