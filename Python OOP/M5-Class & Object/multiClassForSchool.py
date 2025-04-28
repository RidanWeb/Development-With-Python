class Student:

    def __init__ (self, name, cls, id):
        self.name = name
        self.cls = cls
        self.id = id


    def __repr__(self) -> str:
        return f"Name: {self.name}, Class: {self.cls}, ID: {self.id}"
    

class Teacher:

    def __init__ (self, name, sub, id):
        self.name = name
        self.sub = sub
        self.id = id


    def __repr__(self) -> str:
        return f"Name: {self.name}, Subject: {self.sub}, ID: {self.id}"
    


class School:

    def __init__ (self, name) -> None:

        self.name = name
        self.teachers = []
        self.students = []

    def addTeacher(self, name, sub):

        id = len(self.teachers) + 100
        teacher = Teacher(name, sub, id)
        self.teachers.append(teacher)

    def enrollment(self, name, fee):
        
        if fee < 6500:

            return "You must pay the fee of 6500"
        
        else:

            id = len(self.students) + 1
            student = Student(name, 'Math', id)
            self.students.append(student)
            return f"Student {name} has been enrolled in class {student.cls} with ID {id}"
        
    def __repr__(self) -> str:
        print("==========Our Teachers==========")
        for teacher in self.teachers:
            print(teacher)

        print("==========Our Students==========")
        for student in self.students:
            print(student)
        return ""


            


ridan = Student('Rida', 10, 1223)

foisal = Teacher('Faisal', 'Math', 1234)

print(ridan)
print(foisal)

print("\n\n\n")

school = School('Faisal School')
school.addTeacher('Faisal', 'Math')
school.addTeacher('Rida', 'English')
school.addTeacher('Ali', 'Science')

school.enrollment('Rida', 6500)
school.enrollment('Ali', 6000)
school.enrollment('Faisal', 7000)
school.enrollment('Rida', 6500)


print(school)
