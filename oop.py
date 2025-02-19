# OOP stands for object oriented programming
# A Class is a blueprint of ana object
# An Object is an instance of a class
from time import thread_time_ns


class Student:
    def __init__(self, name, age, score):
        self.name=name
        self.age=age
        self.score=score
    # Member Function
    def display(self):
        print(f"Student name is : {self.name}, Age is : {self.age}, Score is: {self.score}")
# Instance of the class (object)
myobj=Student(name="Aisha",age= 18,score='A')
myobj.display()
myobj2=Student(name="Jonathan",age=19,score='B')
myobj2.display()
myobj3=Student(name="Faith",age=17,score='A')
myobj3.display()
myobj4=Student(name="Nathan",age=19,score='B')
myobj4.display()

