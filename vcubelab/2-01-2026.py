'''1. Create a base class Animal with a method sound().
Extend this class with subclasses Dog and Cat, where both provide their specific sound implementations.
Input:Enter animal type: Dog
Output:Dog sound: Bark
class Animal:
    def sound(self):
        pass
class dog(Animal):
    def sound(self):
        return "bark"
class Cat(Animal):
    def sound(self):
        return "eating"
n=input("enter a animal name:")
c=dog()
res=c.sound()
print(res)

2. Develop a base class Vehicle with a method
type_of_vehicle().
Extend this class with subclasses Bike and Car
and provide specific types for each vehicle.
Input:Enter vehicle: Bike
Output:Vehicle Type: Two Wheeler

class Vehicle:
    def type_of_vehicle(self):
        pass
class Bike(Vehicle):
    def type_of_vehicle(self):
        return "Two wheeler"
class Car(Vehicle):
    def type_of_vehicle(self):
        return "four wheeler"
    
n=input("Enter a Vehicle :")
if n=="Bike":
    b=Bike()
elif n=="Car":
    b=Car()
else:
    print("invalid vehicle")
    exit()
print("vehicle type:",b.type_of_vehicle())

3. Design a base class Person with attributes
name and age.
Extend it with subclasses Student and Teacher.
Student has an additional attribute grade,
and Teacher has an attribute subject.
Input:Name: Ravi
Age: 20
Grade: A

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Student(Person):
    def __init__(self,name,age,grade):
        super().__init__(name,age)
        self.grade=grade
class Teacher(Person):
    def __init__(self,name,age,sobject):
        super().__init__(name,age)
        self.subject=subject
name=input("Enter a name:")
age=int(input("Enter a age:"))
grade=input("enter a grade:")
student=Student(name,age,grade)
print("Name:",student.name)
print("Age:",student.age)
print("Grade:",student.grade)'''



        


