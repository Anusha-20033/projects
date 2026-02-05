'''1.strong number or not
---------------------

n=int(input("Enter a number:"))
s=0
bkp=n
while n>0:
    d=n%10
    f=1
    while d>1:
        f=f*d
        d=d-1
    s=s+f
    n=n//10
if s==bkp:
    print("Strong number")
else:
    print("Not strong")
    



2.Write a Python program using a while loop to calculate the sum of the first N natural numbers is even or not.
	Input: 10 
	Output: 55 and ‘Not even’

num=int(input("Enter a number:"))
sum=0
i=1
while i<=num:
    sum=sum+i
    i=i+1
if sum%2==0:
    print(sum,"'and Even'")
else:
    print(sum,"and 'Not Even'")
    


5.even fibanocci series
---------------------------
num=int(input("Enter a number:"))
a=0
b=1
i=1
while i<=num:
    c=a+b
    if c%2==0:
        print(c,end=' ')
        i=i+1
    a=b
    b=c



3.rev a number
---------------
n=int(input("Enter a number:"))
rev=0
while n>0:
    d=n%10
    rev=rev*10+d
    n=n//10
print(rev)



n=int(input("Enter a number:"))
while n>0:
    d=n%10
    print(d,end='')
    n=n//10




4.find the sum of 1 to 100 prime number
----------------------------------------'''




