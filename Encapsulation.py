# class Employee:

#     def __init__(self, name, age, salary):
#         self.name = name
#         self.age = age
#         self.__salary = salary


#     def get_salary(self):
#         return self.__salary
    
#     def inc__salary(self,amount):
#         if amount >0:
#             self.__salary += amount
#             print("Salary updated")
#         else:
#             print("Invalid amount")

# emp= Employee("Priya",25,50000)
# print("Salary:", emp.get_salary())

# emp.inc__salary(8000)
# print("New Balance: ,emp.get_salary()")

# single inheritance

# class animal():

#     def property(self):
#         print("Animals has 4 legs")

#         class Dog(animal):

#             def property(self):
#                 print("Dog barks")
              
              
# d=Dog()

# d.property()
# d.barks()

# multiple inheritance

# class Father:
#     def property(self):
#         print("Driving ")

# class Mother:
#     def property(self):
#         print("Cooking")

# class Child(Father,Mother):
#     def property(self):
#                 print("Inherited skills from both parents")

# x=Child()
# x.Qualities()   
# x.skills()
# x.skills()


# class Grandfather:
#     def house(self):
#         print("Grandfather's House")


# class Father(Grandfather):
#     def bike(self):
#         print("Father's Bike")


# class Son(Grandfather):
#     def laptop(self):
#         print("Son's Laptop")


# class Grandson(Father, Son):
#     def car(self):
#         print("Grandson's Car")


# # Son object
# s = Son()
# s.house()
# s.laptop()

# # Grandson object
# g = Grandson()
# g.house()
# g.bike()
# g.laptop()
# g.car()


# class Institute:

#     def name(self):
#         print("NSTI(W) Allahabad")


#         class Teacher(Institute):
#             pass
#         class Student(Institute):
#             pass
#         class Housekeeping(Institute):
#             pass
#         t=Teacher()
#         s=Student()
#         h=Housekeeping()

#         s.name()
#         T.name()
#         h.name()


            

# Vehicle Management System (Hierarchical Inheritance):

# class Vehicle:
#     def start(self):
#         print("Vehicle is starting")


# class Car(Vehicle):
#     def air_condition(self):
#         print("Car has Air Conditioner")


# class Bike(Vehicle):
#     def helmet_required(self):
#         print("Helmet is required")


# class Bus(Vehicle):
#     def passenger_capacity(self):
#         print("Passenger Capacity: 50")


# c1 = Car()
# b1 = Bike()
# bus1 = Bus()

# c1.start()
# c1.air_condition()

# b1.start()
# b1.helmet_required()

# bus1.start()
# bus1.passenger_capacity()

# Smart Phone System (Multiple Inheritance):

# class Camera:
#     def take_photo(self):
#         print("Taking Photo")


# class MusicPlayer:
#     def play_music(self):
#         print("Playing Music")


# class SmartPhone(Camera, MusicPlayer):
#     def make_call(self):
#         print("Making a Phone Call")


# s1 = SmartPhone()

# s1.take_photo()
# s1.play_music()
# s1.make_call()

# Working Student (Multiple Inheritance)


# class Student:
#     def study(self):
#         print("Student is studying")


# class Employee:
#     def work(self):
#         print("Employee is working")


# class WorkingStudent(Student, Employee):
#     def manage_time(self):
#         print("Managing Study and Work Time")


# w1 = WorkingStudent()

# w1.study()
# w1.work()
# w1.manage_time()

# Company Structure (Hybrid Inheritance)

# class Employee:
#     def attendance(self):
#         print("Employee attendance marked")


# class Developer(Employee):
#     def write_code(self):
#         print("Developer is writing code")


# class Tester(Employee):
#     def test_software(self):
#         print("Tester is testing software")


# class TeamLead(Developer, Tester):
#     def manage_team(self):
#         print("Team Lead is managing team")


# t1 = TeamLead()

# t1.attendance()
# t1.write_code()
# t1.test_software()
# t1.manage_team()

# Educational Institute (Hybrid Inheritance):

