


class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name:{self.name},Age:{self.age}")

student1 = Student("Uzair",21)
student1.display_info()    