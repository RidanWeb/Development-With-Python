import random

class Exam:

    def __init__ (self, name):

        self.name = name
        self.marks = 0

    def getMarks (self):
        self.marks = random.randint(70, 100)
        print("Marks of", self.name, "is", self.marks)



first = Exam("Math")
print(first.getMarks())

