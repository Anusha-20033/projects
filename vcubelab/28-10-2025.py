'''perfect number or not
step1:read a number
step2:find the divisors
step3:sum of the all divisors
step4:compare the sum in to original number
      perfect number
      not perfect number


num=int(input("Enter a number:"))
sum=0
d=1
while d<=num//2:
    if num%d==0:
        sum=sum+d
    d=d+1
if sum==num:
    print("perfect number")
else:
    print("not perfect number")


1.Print Fibonacci Series up to N terms
Input: 7
Output: 0 1 1 2 3 5 8

num=int(input("Enter a number:"))
a=0
b=1
print(a,b,end=' ')
i=1
while i<=num-2:
    c=a+b
    print(c,end=' ')
    i=i+1
    a=b
    b=c



2.Find the sum of first N Fibonacci numbers
Input: 5
Output: 0 + 1 + 1 + 2 + 3 = 7
step1:read the number
step3:sum of the fibanocci series
step4:print the sum


num=int(input("Enter a number:"))
a=0
b=1
s=0
i=0
while i<num:
    c=a+b
    s=s+a
    a=b
    b=c
    i=i+1
print(s)
    
         
    
3.Find the Nth Fibonacci number
Input: 6
Output: 5


num=int(input("Enter a number:"))
a=0
b=1
i=1
while i<num-1:
    c=a+b
    a=b
    b=c
    i=i+1
print(c)





4.Write a Python program to display all the factors of a given number using a while loop.
Input:12
Output:1 2 3 4 6 12

num=int(input("Enter a number:"))
d=1
while d<=num:
    if num%d==0:
        print(d,end=' ')
    d=d+1



5.Write a Python program to display all perfect numbers between 1 and 100 using a while loop.
Ouput: 6   28'''

d=1
while True:
    if 
        
    d=d+1

        








