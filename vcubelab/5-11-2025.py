'''for loops
----------
1.Print numbers from 1 to 10 using for loop
 Output: 1 2 3 4 5 6 7 8 9 10

for i in range(1,11):
    print(i)
    

5.Print sum of numbers from 1 to n using for loop.
 Input: n = 6
 Output: 21

num=int(input("Enter a number:"))
sum=0
for i in range(1,num+1):
    sum=sum+i
print(sum)


9)prime or not by using for loop
---------------------------------
num=int(input("Enter a number:"))
count=0
for i in range(1,num+1):
    if num%i==0:
        count=count+1
if count==2:
    print("prime")
else:
    print("not prime")


num=int(input("Enter a number:"))
for i in range(2,(num//2)+1):
    if num%i==0:
        print("not prime")
        break
else:
    print("prime")


2.Print even numbers from 1 to 20 using for loop.
 Output: 2 4 6 8 10 12 14 16 18 20

for i in range(1,21):
    if i%2==0:
        print(i)

3.Print all numbers from n to 1 (reverse) using for loop.
 Input: n = 5
 Output: 5 4 3 2 1
 
 
num=int(input("Enter a number:"))
for i in range(num,0,-1):
    print(i,end=' ')
    



4.Print squares of numbers from 1 to 10 using for loop.
 Output: 1 4 9 16 25 36 49 64 81 100

for i in range(1,11):
        print(i**2,end=' ')

        
6.Print table of a number using for loop.
 Input: n = 3
 Output: 3 6 9 12 15 18 21 24 27 30

num=int(input("Enter a number:"))
for i in range(1,11):
    print(f"{num*i}",end=' ')


7.Print all odd numbers between 1 and 30 using for loop.
 Output: 1 3 5 ... 29
for i in range(1,31):
    if i%2!=0:
        print(i,end=' ')


8.Print numbers divisible by 3 and 5 (1–50)
 Output: 15 30 45
 
for i in range(1,50):
    if i%3==0 and i%5==0:
        print(i,end=' ')
        

10.Write a Python program using a for loop to find
and print all prime numbers between 10 and 50 ?      
n=int(input("Enter a number:"))
num=10
for i in range(10,50):
    for j in range(2,(num//2)+1):
        if num%j==0:
            break
        j=j+1
    else:
        print(num,end=' ')
    num=num+1'''
        
    
    
    
    


