'''1. Write a Python program to  factorial of given number.
Input:5
Output:120

num=int(input("Enter a number:"))
f=1
while num>1:
    f=f*num
    num=num-1
print(f)


2. Write a Python program to generate and print a random even number between 50 and 100
import random
res=random.randrange(50,101,2)
print(res)


3. Generate a random number between 1 and 100 and print whether it is odd or even.
import random
res=random.randrange(1,101,2)
print(res)


4. Write a python program to find smallest digit in  given number
Input:456378
Output:3

num=int(input("Enter a number"))
small=100
while num>0:
    t=num%10
    if t<small:
        small=t
    num=num//10
print(small)


5. Write a python program to convert the number to binary digits?
Input: 6
Output: 110

num=int(input("Enter a number"))
res=bin(num)
print(res)


num=int(input("Enter a number"))
res=(bin(num)[2:])
print(res)


num=int(input("Enter a number:"))
bin=0
place=1
while num>0:
    t=num%2
    bin=bin+t*place
    place=place*10
    num=num//2
print(bin)




6.Write a python program to find n th prime number?
Input: 6
Output: 13'''
num=int(input("Enter a number"))







'''7. Write a python program using while loop to calculate the sum of the first N natural numbers is even or not.
Input:10
Output:55   and ‘Not Even’
num=int(input("Enter the number:"))
sum=0
i=1
while i<=num:
    sum=sum+i
    i=i+1
print(sum)
if sum%2==0:
    print("Even")
else:
    print("Not Even")'''









