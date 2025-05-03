class Person:

    #class attribute/ static attribute which is shared by all instances of the class

    skills = [] # class attribute

    def __init__(self, name, age, height, weight):
        self.name = name # instance attribute
        self.age = age #instance attribute
        self.height = height # instance attribute
        self.weight = weight # instance attribute


    # instance method
    def eat(self, item, amount, price):
        print(f"{self.name} eats {item} {amount} kg for {price} tk")   

     # class method
    @classmethod
    def myJobs(self, position, salary):
        print(f"{position} earns {salary} tk per month")

    
    # static method
    @staticmethod #used to define a method that does not depend on class or instance
    def myCountry(country):
        print(f"{country} is a beautiful country")


redan = Person("Redan", 25, 5.8, 70)

redan.eat("rice", 2, 50)
redan.myJobs("Software Engineer", 50000)
# Person.eat("fish", 1, 100)

Person.myJobs("Software Engineer", 50000)
