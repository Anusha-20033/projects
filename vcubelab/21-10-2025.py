'''LCD
--------

Algorithm

s1:read the two number
s2:find small number
s3:find the divisors
s4:decide LCD



n1=int(input("enetr a anumber"))
n2=int(input("enter a another number"))
if n1<n2:
    small=n1
else:
    small=n2
d=2
while d<=small:
    if n1%d==0 and n2%d==0:
        print("LCD IS",d)
        break
    d=d+1
else:
    print("no LCD")


1)Write a Python program to find the sum of numbers from 1 to n.
 Input: 5
 Output: 15


num=int(input("Enter a number"))
i=1
sum=0
while i<=num:
    sum=sum+i
    i=i+1
print(sum)



GCD
-----
s1:read two number
s2:find the smallest number
s3:find the divisors starting from small
s4:decide GCD'''


n1=int(input("Enter a number"))
n2=int(input("Enter a another number"))
if n1<n2:
    small=n1
else:
    small=n2
d=2
while small>=d:
    if n1%d==0 and n2%d==0:
        print("GCD",n1)
        break
    d=d+1
else:
    print(" no GCD")


'''2.Write a Python program to count the digits in a number.
Input: 12345
 Output: 5

num=int(input("enter a number"))
count=0
while num>0:
    num=num//10
    count=count+1
print(count)



3.Write a Python program to print odd numbers from 1 to 15.
Output: 1 3 5 7 9 11 13 15

num=int(input("Enter a number"))
i=1
while i<=num:
    if i%2!=0:
        print(i)
    i=i+1


4.Write a Python program to find the largest digit in a number.
 Input: 84539
 Output: 9

num=int(input("Enter a number"))
big=0
while num>0:
    t=num%10
    if t>big:
        big=t
    num=num//10
print(big)
        
    



5.Write a python program to Find the smallest digit in a number
 Input: 245
 Output: 2

num=int(input("Enter a number"))
small=100
while num>0:
    t=num%10
    if t<small:
        small=t
    num=num//10
print(small)


 


6.Write a python program to print LCD of two numbers.
Input: n1=15  n2=20 
Output: 60


7.Count the number of even and odd digits in a number.
Input: 24561
Output: Even: 3  Odd: 2



8.Write a python program to reverse given number.
Input:123
Output:321

num=int(input("enter the number"))
rev=0
while num>0:
    t=num%10
    rev=(rev*10)+t
    num=num//10
print(rev)


9.Write  a python program to check whether given number is Prime number or not.
Input:5
Output: Prime number

num=int(input("Enter a number"))
d=2
while d<=num//2:
    if num%d==0:
        print("not a prime")
        break
    d=d+1
else:
    print("prime")'''

























 

