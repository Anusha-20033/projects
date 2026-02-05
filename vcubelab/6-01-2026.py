'''1. Write a Python program to demonstrate method overriding using a base class Bird with a method sound().
Create derived classes Parrot and Crow that override the sound() method to display their respective sounds.
Output:Parrot says: Squawk
Crow says: Caw Caw
class Bird:
    def sound(self):
        pass
class Parrot(Bird):
    def sound(self):
        print("Parrot says:Squawk")
class Crow(Bird):
    def sound(self):
        print("Crow says: CawCaw")
b=Parrot()
c=Crow()
b.sound()
c.sound()

2. Write two classes Dog and Cat, each having a common method speak().
Create a function animal_sound(obj) that accepts any object and calls its speak() method to demonstrate polymorphism.
Output:Dog says: Bark
Cat says: Meow
class Dog:
    def speak(self):
        print("Dog says: Bark")
class Cat(Dog):
    def speak(self):
       print("Cat says: Meow")
def animal_sound(obj):
    obj.speak()
d=Dog()
c=Cat()
animal_sound(d)
animal_sound(c)

3. Create a class Animal with a method eat().Derive class Mammal from Animal and class Dog from Mammal.Call all methods using a Dog object.
OutPut;Animal is eating
Mammal is breathing
Dog is barking

class Animal:
    def eat(self):
        print("Animal is eating")
class Mammal(Animal):
    def breathe(self):
        print("Mammal is breathing")
class Dog(Mammal):
    def bark(self):
        print("Dog is barking")
d=Dog()
d.eat()
d.breathe()
d.bark()'''


    
    




