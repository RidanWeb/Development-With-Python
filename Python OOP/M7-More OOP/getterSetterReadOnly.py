class user:
    def __init__(self, name, age, money):
        self.name = name
        self.age = age
        self.__money = money

    @property
    def money(self):
         return self.__money
    
    @money.setter
    def setMoney(self, money):
        self.__money += money



    def getMoney(self):
         return self.__money



me = user("Ridan", 20, 25000)

# print(me.name)
# print(me.age)
print(me.money)
print(me.getMoney())
me.setMoney = 5000
print(me.money)

