class Phone:
    name = "Samsung"
    color = "Red"
    price = 200000000

    def demo(self):

        print("This is normal demo class")

    def add(self, first, sec):

        sum = f"Sum of two num is {first+sec} taka"
        print (sum)

    def sub(self, first, sec):

        sub = f"Sub of two num is {first+sec} taka"
        print (sub)

    def mul(self, first, sec):

        mul = f"Multi of two num is {first+sec} taka"
        return mul

    


myPhone = Phone()

print(myPhone.name)
print(myPhone.color)
print(myPhone.price)

myPhone.demo()
myPhone.add(20, 50)
myPhone.sub(200, 50)
print(myPhone.mul(5, 9))