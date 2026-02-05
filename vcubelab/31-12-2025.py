'''1.Write a Python program to find all prime factors
of a given number
Input:Enter a number: 84
Output:Prime factors: 2 2 3 7

n=int(input("Enter number"))
i=2
print("Prime factors:",end=' ')
while n>1:
    if n%i==0:
        print(i,end=' ')
        n=n//i
    else:
        i=i+1

2.Write a program to count the number of prime factors (with repetition).
Input:Enter a number: 60
Output:Total prime factors: 4

n=int(input("Enter a number:"))
i=2
count=0
while n>1:
    if n%i==0:
        count+=1
        n=n//i
    else:
        i+=1
print("Total prime factors:",count)

3.Write a program to find the largest prime factor
of a number.
Input:Enter a number: 13195
Output:Largest prime factor: 29

n=int(input("Enter a number:"))
i=2
largest=0
while n>1:
    if n%i==0:
        largest=i
        n=n//i
    else:
        i=i+1
print("Largest prime factor:",largest)

5.Write a Python program using a class to
find the length of a string.
Input:Enter string: Python
Output:Length of string: 6

class Length:
    def __init__(self,string):
        self.string=string
    def display(self):
        return len(self.string)
l=Length("python")
res=l.display()
print(res)

6.Create a class to reverse a string without
using built-in functions.
Input:Enter string: hello
Output:Reversed string: olleh

class Reverse:
    def __init__(self,string):
        self.string=string
    def display(self):
        output=""
        for i in self.string:
            output=i+output
        return output
string=input("enter a string:")
r=Reverse(string)
print("Reversed string:",r.display())

7.Write a program using a constructor to count
vowels in a string.
Input:Enter string: education
Output:Vowel count: 5'''

class Vowels:
    def __init__(self,string):
        self.string=string
        self.count=0
        for i in self.string:
            if i.lower() in "aeiou":
                self.count+=1
    def display(self):
        print("vowels count:",self.count)
string=input("enter a string:")
v=Vowels(string)
v.display()

        
        
        








