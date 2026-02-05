'''fibanocci series
-------------------------
a=0
b=1
print(a,end=' ')
print(b,end=' ')
i=1
while i<=5:
    c=a+b
    print(c,end=' ')
    a=b
    b=c
    i=i+1

even fibanocci number
--------------------
num=int(input("Enter a number:"))
count=1
a=0
b=1
while True:
    c=a+b
    if c%2==0:
        count=count+1
        if count==num:
            print(c)
            break
    a=b
    b=c
    
        


enter a character:z
enter a character is z

enter a character:c
enetr a character:C
enetr a character:y
enter a character is y

enter a character:b
enetr a character:B



while True:
    ch=input(" Enter a character:")
    if ch=='c' or ch=='C':
        continue
    if ch=='b' or ch=='B':
        break
    print("enter a characted is",ch)



1.Write a Python program to find the largest digit in a number.
 Input: 84539
 Output: 9
 

n=int(input("Enter a number"))
big=0
while n>0:
    t=n%10
    if t>big:
        big=t
    n=n//10
print(big)


2. Write a python program to find smallest digit in  given number
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


3.Write a python program to check whether given number is perfect or not
Input:6
Output: Perfect number

num=int(input("Enter a Number:"))
i=0
d=1
while d<num:
    if num%d==0:
        i=i+d
    d=d+1
if i==num:
    print(num,"is a perfect number")
else:
    print(num,"is not a perfect number")
        





4.Write a Python program to find the sum of even numbers from 1 to 50.
 Output: 650

num=int(input("Enter a number:"))
i=1
sum=0
while i<=num:
    if i%2==0:
        sum=sum+i
    i=i+1
print(sum)


5.Write a Python program to print the Fibonacci series up to n terms. Input: 6
 Output: 0 1 1 2 3 5

num=int(input("Enter a number:"))
a=0
b=1
print(a,b,end=' ')
i=1
while i<=num-2:
    c=a+b
    print(c,end=' ')
    a=b
    b=c
    i=i+1


6.Write a Python program using a while loop to calculate the sum of the first N natural numbers is even or not.
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




#to check whether it is fibanocci number or not
num=int(input("Enter a number:"))
a=0
b=1
while True:
    c=a+b
    if c==num:
        print(num,"is fibanocci number")
        break
    if c>num:
        print(num," is Not fibanocci number")
        break
    a=b
    b=c



#nth prime fibanocci number'''
num=int(input("Enter a number:"))
a=0
b=1
while True:
    c=a+b
    if c!=1:
        while num<=c//2:
            if num%c==0:
                break
            c=c+1
        num=num//10
    else:
        if c==num:
            print
    
a=b
b=c

    


    






    
    


