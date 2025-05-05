import random
from school import School

class Person:

    def __init__(self, name):
        self.name = name


class Teacher(Person):

    def __init__(self, name, subject):
        super().__init__(name)

    def evaluate_exam(self):
        
        return random.randint(0, 100 )
    

class Student(Person):

    def __init__(self, name, classroom):
        super().__init__(name)
        self.classroom = classroom
        self.__id = None
        self.marks = {} #{"Eng": marks, "Math": marks, "Science": marks}
        self.sub_grades = {} #{"Eng": grade, "Math": grade, "Science": grade}
        self.final_grade = None

    def calculate_final_grade(self):

        sum = 0
        for grade in self.sub_grades:

            point = School.grade_to_value(grade)
            sum += point

        gpa = sum / len(self.sub_grades)

        self.final_grade = School.value_to_grade(gpa)

    
    @property
    def get_id(self):

        return self.__id

    @id.setter
    def set_id(self, value):

        self.__id = value


