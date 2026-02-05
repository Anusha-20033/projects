'''2.Write a Python program to reverse a given number.
Input:123
Output:321
n=int(input("Enter a number:"))
rev=0
while n>0:
    t=n%10
    rev=(rev*10)+t
    n=n//10
print(rev)

4.Write a lambda function to reverse a string.
input:text = "hello"
output:olleh

st=lambda x:x[::-1]
print(st("hello"))

st="hello"
output=""
for i in st:
    output=i+output
print(output)

3.Write a lambda function to find the square of a number.
input:num = 7
output:49
square=lambda x:x**2
print(square(7))

5.Write a lambda function to check if a string
is a palindrome.
Input:”madam”
output:True

palindrome=lambda x:x==x[::-1]
print(palindrome("madam"))

6.Write a lambda function to calculate the
length of a string.
input:text = "Lambda"
Output:6

string=lambda x:len(x)
print(string("Lambda"))

7.Write a lambda function to extract the first
character from a string.
input:text = "hello"
Output:h

text=lambda x:x[0]
print(text("hello"))

8.Write a Python program using a decorator
to remove duplicate characters from
the returned string.
Input: "aabbccdde"
 Output: abcde
def duplicate(fun):
    def wraperfun():
        st=""
        for i in fun():
            if i not in st:
                st=st+i
        print(st)
    return wraperfun
@duplicate
def display():
    return "aabbccdde"
display()

9.Write a Python decorator that measures how
long a function takes to run and prints the
execution time.
output:Task complete  
Execution time: 0.0563 seconds
import time
def defun(fun):
    def wraperfun():
        start=time.time()
        fun()
        end=time.time()
        print(f"Execution time:{end-start:.4f}seconds")
    return wraperfun
@defun       
def display():
    time.sleep(0.05)
    print("Task complete")
display()

1.Write a Python program to print numbers
from 1 to 100, but skip the numbers whose
digit-sum is a prime number.
Example: 29 → 2+9 = 11 (prime) → skip

n=int(input("Enter a number:"))
num=1
while num<=100:
    d=2
    while d<=num//2:
        if num%d==0:
            break
        d=d+1
    else:
        print(num,end=" ")
    num=num+1'''


reverse=lambda x:int(x[::-1])
print(reverse("123"))






   
