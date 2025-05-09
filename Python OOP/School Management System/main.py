from school import School
from person import Student,Teacher
from subject import Subject
from classroom import ClassRoom


school = School("Jamil's School", "Ghoraghat")


eight = ClassRoom("Eight")
nine = ClassRoom("Nine")
ten = ClassRoom("Ten")



school.add_class_room(eight)
school.add_class_room(nine)
school.add_class_room(ten)

rahima = Student("Rahims", ten)
karima = Student("Karima", nine)
sarima = Student("Sarima", eight)
ridan = Student("Ridan", nine)



school.student_admission(rahima)
school.student_admission(karima)
school.student_admission(sarima)
school.student_admission(ridan)



jamil = Teacher("Jamil Khan")
kamil = Teacher("Kamil Bahadur")
hamil = Teacher("Hamil Shekh")
samil = Teacher("Samil Rahaman")



bangla = Subject("Bangla", jamil)
english = Subject("English", kamil)
math = Subject("Math", hamil)
physics = Subject("Physics", samil)
social = Subject("Social", samil)


eight.add_subject(bangla)
eight.add_subject(math)
eight.add_subject(physics)
nine.add_subject(physics)
nine.add_subject(social)
nine.add_subject(math)
ten.add_subject(bangla)
ten.add_subject(english)
ten.add_subject(math)
ten.add_subject(physics)



eight.semester_final_exam()
nine.semester_final_exam()
ten.semester_final_exam()


print(school)
