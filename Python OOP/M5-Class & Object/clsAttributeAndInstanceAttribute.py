class Shop:

    card = []  # class attribute

    def __init__ (self, name):
        self.name = name
    

    def addCard (self, card):
        self.card.append(card)


# class attribute is shared by all instances of the class
mrX= Shop("Mr. X")
mrX.addCard("Ie cream")
mrX.addCard("Chocolate")
mrX.addCard("Drinks")

print(mrX.card)

mrY = Shop("Mr. Y")
mrY.addCard("Cake")
mrY.addCard("Banana")
mrY.addCard("Biscuits")

print(mrY.card)




class ShopAgain:

    def __init__ (self, name):
        self.name = name
        self.card = []  # instance attribute

    def addCard (self, card):
        self.card.append(card)



# instance attribute is unique to each instance of the class
mrA= ShopAgain("Mr. X")
mrA.addCard("Ie cream")
mrA.addCard("Chocolate")
mrA.addCard("Drinks")

print(mrA.card)

mrB = ShopAgain("Mr. B")
mrB.addCard("Cake")
mrB.addCard("Banana")
mrB.addCard("Biscuits")

print(mrB.card)
