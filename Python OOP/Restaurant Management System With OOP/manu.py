class Manu:



    def __init__(self):

        self.items = []

    def add_item(self, item):

        self.items.append(item)
        print(f"Item {item.name} added to the menu.")

    def find_item(self, item_name):

        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return False
    
    def remove_item(self, item_name):

        hasItem = self.find_item(item_name)

        if hasItem:
            self.items.remove(hasItem)
            print(f"Item {item_name} removed from the menu.")
        else:
            print(f"Item {item_name} not found in the menu.")   


    def view_items(self):

        if not self.items:
            print("No items found in the menu.")
        else:
            print("***********Menu Items***********")

            print(f"Name\tPrice\tQuantity")
            for item in self.items:
                
                print(f"{item.name}\t{item.price}\t{item.quantity}")


   