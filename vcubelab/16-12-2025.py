'''variable key arguments
=======================
1)list-key arguments
2)dictinary of keywords arguments

def display(a,b,*args,c=50,**kwargs):
    print("mandatory input:",a,b)
    print("default arguments:",c)
    print("optional aruguments:",args)
    print("dictinary arguments:",kwargs)
display(10,30,'vcube',True,30,name='anu',age=40)

SCOPE
========
1)local
2)global
3)non local
4)built in

Global
=======
x=10#global it can store a heap in memory allocation
def display():
    y=20#local
    print(x)
    print(y)
display()
print(x)
print(y)#error i can store a stack block


x=10
def display():
    global x
    x=50
    print(x)
    y=40
    print(y)
display()
print(x)
    

Local
======
def display():
    x=20
    print(x)
display()


NESTED FUNCTIONS
===================
def outerfun():
    print("anu")
    #innerfun()#error
    def innerfun():
        print("anusha")
    innerfun()#anusha
outerfun()#anu
#innerfun()#error


1.Write a function to check whether a string is
a palindrome.
Input: "madam"
Output: Palindrome

def palindrome(st):
    if st==st[::-1]:
        print("Palindrome")
    else:
        print("not palindrome")
    
st=input("Enter a string:")
palindrome(st)



6.Write a function to reverse a string.
Input: "python"
Output: "nohtyp"

def reverse(st):
    output=""
    for i in st:
        output=i+output
    return output
st=input("enter a string:")
output=reverse(st)
print(output)


5.Write a function to find the first non-repeating
character in a string.
Input: "programming"
Output: p

def first(st):
    for i in st:
        if st.count(i)==1:
            return  i
            break
st=input("Enter a string:")
res=first(st)
print(res)


7.Write a function to calculate the factorial of
a number.
Input: 5
Output: 120

def factional(num):
    fact=1
    while num>=1:
        fact=fact*num
        num=num-1
    return fact
num=int(input("Enter a number:"))
fact=factional(num)
print(fact)


4.Write a function to check whether a number
is an Armstrong number.
Input: 153
Output: Armstrong Number

def digitcount(num):
    count=0
    bkp=num
    while num>0:
        num=num//10
        count+=1
    num=bkp
def multiplecubes(num):
    count=3
    sum=0
    bkp=num
    while num>0:
        t=num%10
        sum=sum+t**count
        num=num//10
    if sum==bkp:
         return "armstrong"
    else:
         return  "not armstrong"
num=int(input("Enter a number:"))
res=digitcount(num)
res1=multiplecubes(num)
print(res1)


3.Write a function to find all prime numbers
between two numbers.
Input: 10, 30
Output: 11 13 17 19 23 29

def primenumber(num2):
    num1=10
    for i in range(num1,num2):
        for j in range(2,(num1//2)+1):
            if num1%j==0:
                break
        else:
            print(num1,end=' ')
        num1=num1+1
    return num1
num2=int(input("Enter a end sequence number:"))
primenumber(num2)


2.Write a function to count words in a sentence.
Input: "Python is easy to learn"
Output: 5

def countwords(st):
    words=st.split()
    str=len(words)
    return str
st="Python is easy to learn"
str=countwords(st)
print(str)

8.Write a function to calculate the square and cube of a number

def square_cube(num):
    square=num**2
    cube=num**3
    return square,cube
num=int(input("enter a number:"))
square,cube=square_cube(num)
print(square,cube,end=' ')'''
