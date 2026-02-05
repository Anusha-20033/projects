'''1.Design a base class Fruit with an attribute taste.
Extend this class with subclasses Apple and Orange, setting their specific taste in constructors.
Input:
apple = Apple()
orange = Orange()
print(apple.taste)
print(orange.taste)
Output:
Sweet
Citrus

class Fruit:
    def __init__(self,taste):
        self.taste=taste

class Apple(Fruit):
    def __init__(self):
        super().__init__("sweet")
class Orange(Fruit):
    def __init__(self):
        super().__init__("citrus")
apple=Apple()
orange=Orange()
print(apple.taste)
print(orange.taste)

2.Create a base class Bird with a method fly().
Extend this class with subclasses Sparrow and Ostrich.
Sparrow can fly, Ostrich cannot.
Input:
s = Sparrow()
o = Ostrich()
s.fly()
o.fly()
Output:
Sparrow can fly
Ostrich cannot fly

class Bird:
    def fly(self):
        pass
class Sparrow(Bird):
    def fly(self):
        print("Sparrow can fly")
class Ostrich(Bird):
    def fly(self):
        print("Ostrich cannot fly")
s = Sparrow()
o = Ostrich()
s.fly()
o.fly()

3.Develop a base class Shape with a method area().
Extend this class with subclasses Square and Circle.
Input:
sq = Square(4)
ci = Circle(7)
print(sq.area())
print(ci.area())
Output:
16
153.94

class Shape:
    def area(self):
        pass
class Square(Shape):
    def __init__(self,side):
        self.side=side
        
    def area(self):
        return self.side*self.side
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return round(3.14*self.radius*self.radius,2)
sq = Square(4)
ci = Circle(7)
print(sq.area())
print(ci.area())

4. Design a base class Person with attributes name and age.
Extend this class with Student (grade) and Teacher (subject).
Input:
s = Student("Ravi", 20, "A")
t = Teacher("Sita", 35, "Math")
print(s.details())
print(t.details())
Output:
Name: Ravi, Age: 20, Grade: A
Name: Sita, Age: 35, Subject: Math

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
class Student(Person):
    def __init__(self,name,age,grade):
        super().__init__(name,age)
        self.grade=grade
    def details(self):
        return f"Name:{self.name},Age:{self.age},Grade:{self.grade}"
    
class Teacher(Person):
    def __init__(self,name,age,subject):
        super().__init__(name,age)
        self.subject=subject
    def details(self):
        return f"Name:{self.name},Age:{self.age},Subject:{self.subject}"
    
s = Student("Ravi", 20, "A")
t = Teacher("Sita", 35, "Math")
print(s.details())
print(t.details())'''

        



    
        
        




    

        
