'''1. Write a program to calculate and display the grade of a student based on the given marks.
Grading Criteria (Example):
Marks ≥ 80 → Grade A
Marks ≥ 60 and < 80 → Grade B
Marks ≥ 40 and < 60 → Grade C
Marks < 40 → Grade F

marks=int(input("Enter a number:"))
if marks>=80:
    print("Grade A")
elif marks>=60 and marks<80:
    print("Grade B")
elif marks>=40 and marks<60:
    print("Grade C")
else:
    print("Grade F")

2. Write a Python program to print the multiplication table of a given number.
Input: 5
Output: 5 10 15 20 25 30 35 40 45 50
n=int(input("Enter a number:"))
for i in range(1,11):
    print(n*i,end=' ')

3. Write a Python program to reverse a given number.
Input: 1234
Output: 4321
n=int(input("Enter a number:"))
rev=0
while n>0:
    d=n%10
    rev=rev*10+d
    n=n//10
print(rev)
4. Write a Python program to flatten a 2D list into a single list.?
Input:matrix = [[1, 2], [3, 4], [5, 6]]
output:[1, 2, 3, 4, 5, 6]
matrix=[[1, 2], [3, 4], [5, 6]]
flat=[]
for i in matrix:
    for item in i:
        flat.append(item)
print(flat)

5. Write a Python program to find all the prime numbers in a given list.
Input:lst = [1, 2, 3, 4, 5, 10, 13, 15, 17]
output:[2, 3, 5, 13, 17]

lst=[1, 2, 3, 4, 5, 10, 13, 15, 17]
prime=[]
for num in lst:
    if num>1:
        for i in range(2,(num//2)+1):
            if num%i==0:
                break
        else:
            prime.append(num)
print(prime)
6. Write a Python program to sort a dictionary by its values.
           Input: {'a': 3, 'b': 1, 'c': 2}
           Output: {'b': 1, 'c': 2, 'a': 3}
7. Write a Python program to print all possible substrings of a given string.
Input:abc
output:['a', 'ab', 'abc', 'b', 'bc', 'c']
number="abc"
list=[number[i:j]for i in range(len(number)) for j in range(i+1,len(number)+1)]
print(list)

8. Write a Python decorator that converts the output of a function to lowercase.
input:"ALICE"
Output:alice
def decorator(fun):
    def wrapper():
        return fun().lower()
    return wrapper
@decorator
def display():
    return "ALICE"
p=display()
print(p)

9. Write a Python generator function to yield Fibonacci numbers up to n terms.
input:n = 6
output:0 1 1 2 3 5
def fibanacci(n):
    a,b=0,1
    for i in range(n):
        yield a
        a,b=b,a+b
for num in fibanacci(6):
    print(num,end=" ")

10. Write a recursive function in Python to add the digits of a number until a single digit remains.
input:1234
Output:1'''

