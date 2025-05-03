class StudentDatabase:

    student_list = []

    # def __init__(self):

    #     self.student_list = [] 



    @staticmethod
    def add_student(student):

        StudentDatabase.student_list.append(student)

class Student:

    def __init__(self, studentId, name, department, isEnrolled):

        self.__studentId = studentId
        self.__name = name
        self.__department = department
        self.__isEnrolled = isEnrolled




    @property
    def studentIdM(self):
        return self.__studentId
    
    @property
    def nameM(self):
        return self.__name
    
    @property
    def departmentM(self):
        return self.__department
    
    @property
    def isEnrolledM(self):
        return self.__isEnrolled


    @isEnrolledM.setter
    def enroll_studentM(self, stdId):

         for student in StudentDatabase.student_list:
            if student.studentIdM == stdId :
                if student.isEnrolledM == False:
                    self.__isEnrolled = True
                    break

    @isEnrolledM.setter
    def drop_studentM(self, stdId):

        for student in StudentDatabase.student_list:
            if student.studentIdM == stdId :
                if student.isEnrolledM == True:
                    self.__isEnrolled = False
                    break

    

    def view_student_info(self):

        print(f"Student ID: {self.__studentId}, Name: {self.__name}, Department: {self.__department}, Enrolled: {self.__isEnrolled}")


firstS = Student(223, "Redan", "CSE", True)
secondS = Student(224, "Rafiq", "EEE", True)
thirdS = Student(225, "Rafiq", "BBA", False)


StudentDatabase.add_student(firstS)
StudentDatabase.add_student(secondS)
StudentDatabase.add_student(thirdS)



print("Student Management System")
print("1. View All Students")
print("2. Enroll Student")
print("3. Drop Student")
print("4. Exit")

choice = 0

while choice != 4:

    choice = int(input("Enter your choice: "))
    found  = False

    if choice == 1:

        print("All Students:")
        for student in StudentDatabase.student_list:
            student.view_student_info()

    elif choice == 2:

        stdId = int(input("Enter Student ID: "))

        for student in StudentDatabase.student_list:
        
            if student.studentIdM == stdId :

                if student.isEnrolledM == False:
                    student.enroll_studentM = stdId
                    print(f"Student {student.nameM} enrolled successfully.")
                    found = True
                    break
                else:
                    print(f"Student {student.nameM} is already enrolled.")
                    found = True
                    break

        if not found:
            print("Student not found.")

                

    elif choice == 3:

        stdId = int(input("Enter Student ID: "))

        for student in StudentDatabase.student_list:
        
            if student.studentIdM == stdId:

                if student.isEnrolledM == True:
                    student.drop_studentM = stdId
                    print(f"Student {student.nameM} dropped successfully.")
                    found = True
                    break

                else:
                    print(f"Student {student.nameM} is not enrolled.")
                    found = True
                    break


        if not found:
            print("Student not found.")

