class School:

    def __init__(self, name, address):
        self.name = name
        self.address = address

        self.teachers = {}
        self.class_rooms = {}

    
    def add_class_room(self, classroom):

        self.class_rooms[classroom.name] = classroom
        print(f"Classroom {classroom.name} added to {self.name}.")

    def add_teacher(self, subject, teacher):

        if subject in self.teachers:
            self.teachers[subject.name].append(teacher)
        else:
            self.teachers[subject.name] = [teacher]

        print(f"Teacher {teacher.name} added to {self.name} for subject {subject}.")

    
    def student_admission(self, student):

        class_name = student.classroom.name
        self.class_rooms[class_name].add_student(student)




    @staticmethod
    def calculate_grade(marks):
        if marks >= 90 and marks <= 100:
            return "A+"
        elif marks >= 80 and marks < 90:
            return "A"
        elif marks >= 70 and marks < 80:
            return "B+"
        elif marks >= 60 and marks < 70:
            return "B"
        elif marks >= 50 and marks < 60:
            return "C+"
        elif marks >= 40 and marks < 50:
            return "C"
        else:
            return "F"
        
    @staticmethod
    def grade_to_value(grade):

        if grade == "A+":
            return 4.0
        elif grade == "A":
            return 3.7
        elif grade == "B+":
            return 3.3
        elif grade == "B":
            return 3.0
        elif grade == "C+":
            return 2.7
        elif grade == "C":
            return 2.0
        else:
            return 0.0
        
    @staticmethod
    def value_to_grade(value):

        if value == 4.0:
            return "A+"
        elif value >= 3.7:
            return "A"
        elif value >= 3.3:
            return "B+"
        elif value >= 3.0:
            return "B"
        elif value >= 2.7:
            return "C+"
        elif value >= 2.0:
            return "C"
        else:
            return "F"
        
    def __repr__(self):
        
        print("===========All Students==========")

        result = ""

        for key, value in self.class_rooms.items():

            result += f"{key.upper()} ClassRoom Students\n"

            for student in value.students:

                result += f"{student.name}\n"

        print(result)


        print("===========All Subjects==========")

        subject = ""

        for key, value in self.class_rooms.items():

            subject += f"{key.upper()} ClassRoom Subjects\n"

            for sub in value.subjects:

                subject += f"{sub.name}\n"

        print(subject)


        print("Students Marks\n")

        for key, value in self.class_rooms.items():
            for student in value.students:
                for k, i in student.marks.items():
                    print(student.name, k, i, student.sub_grades[k])
                x = student.calculate_final_grade()
                print(x)

        return ''

        
             