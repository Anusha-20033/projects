'''1.sum of first n natural number
num=int(input("Enter a n value"))
sum=0
i=1
while i<=num:
    sum=sum+i
    i=i+1
print(sum)


2.factorial number
num=int(input("enter the number"))
f=1
while num>1:
    f=f*num
    num=num-1
print(f)


3.divisors of the given number
num=int(input("enter a number"))
d=1
while d<=num:
    if num%d==0:
        print(d)
    d=d+1
    

1.Write a program to check if a number is divisible by both 2 and 3.

num=int(input("Enter a number"))
if num%2==0 and num%3==0:
    print(num,"it is divible by 2 and 3")
else:
    print(num,"it is not divisible by 2 and 3")


2.Write a Python program to check whether a given year is a leap year or not.
Input:2024
Output: Leap year
num=int(input("Enter the number"))
if (num%4==0 and num%100!=0) or (num%400==0):
    print("leap year")
else:
    print("not leap year")



4).Write a Python program to swap two numbers without using a third variable.
Input: a=67,b=76
Output: a=76,b=67

a=67
b=76
b,a=a,b
print(a)
print(b)


5.Write a Python program to find the square root of a given number.
Input:4
Output:16
i=int(input("Enter a number"))
root=i**2
print(root)'''


















