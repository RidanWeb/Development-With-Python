class Shopping:

    def __init__ (self, name):
        self.name = name
        self.card = []  # instance attribute

    def addToCard(self, item, price, quantity):
        product = {'item' : item, 'price' : price, 'quantity' : quantity}
        self.card.append(product)

    
    def checkOut(self, amount):
        total = 0

        for product in self.card:

            total += product['price'] * product['quantity']

        if(amount < total):
            print(f"Not enough money. YOu need more {total - amount} to buy the items in your card.")
        elif(amount >= total):
            print(f"Thank you for shopping with us. Your total is {total} for {product['item']} and your change is {amount - total}.")
        



mrX= Shopping("Mr. X")
mrX.addToCard("Ice cream", 200, 2)
mrX.addToCard("Chocolate", 100, 3)
mrX.addToCard("Drinks", 50, 5)

mrX.checkOut(20000)
print(mrX.card)