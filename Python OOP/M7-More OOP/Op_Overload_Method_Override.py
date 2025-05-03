class Person:
    def __init__(self, name, age, height, weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def eat(self):
        print(f"{self.name} is eating Heavily food  and his weight is {self.weight} kg")

    def exercise(self):
        raise NotImplementedError("This method should be overridden in subclasses")



    

class Cricketer(Person):

    def __init__(self, name, age, height, weight, team):
        super().__init__(name, age, height, weight)
        self.team = team

    def eat(self):
        print("Eat vegetables and fruits")

    def exercise(self):
        print(f"{self.name} Exercise regularly")


        # dunder method python=================

    def __add__(self, other):
        return self.age + other.age
    
    def __mul__(self, other):
        return self.weight * other.weight
    
    def __gt__(self, other):
        return self.age > other.age
    
    def __lt__(self, other):
        return self.age < other.age

    




shakib = Cricketer("Shakib", 36, 5.8, 70, "Bangladesh")
shakib.eat()



tamim = Cricketer("Tamim", 34, 5.9, 75, "Bangladesh")
tamim.exercise()

print(shakib.__dict__)
print(tamim.__dict__)

#plusm sign overloading
print(shakib.age + tamim.age)
print(shakib.weight + tamim.weight)
print(shakib.age - tamim.age)







print(shakib < tamim)
print(shakib.weight > tamim.weight) 