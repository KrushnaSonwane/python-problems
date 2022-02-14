# Problem 34 Solution
# 
class Student():
    def name(self):
        print('Patil')
    def city(self):
        print('Pune')
    def type(self):
        print('Science')

class Teacher():
    def name(self):
        print('Rajguru')
    def city(self):
        print('Aurangabad')
    def type(self):
        print('Art')

student_obj = Student()
teacher_obj = Teacher()
for i in (student_obj, teacher_obj):
    i.name()
    i.city()
    i.type()