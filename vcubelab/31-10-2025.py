'''2.Write  a python program to count Even digits?
Input: 123456789
Output: 4

n=int(input("Enter a numbers"))
count=0
while n>0:
    t=n%10
    if t%2==0:
        count=count+1
    n=n//10
print(count)




3. Write a Python program to print all Perfect Numbers between 1 and 100.
Output:6  28

num=1
while num<=100:
    sum=0
    i=1
    while i<num:
        if num%i==0:
            sum=sum+i
        i=i+1
    if sum==num:
        print(num,end='  ')
    num=num+1
    


num=1
while num<=1000:
    sum=0
    i=1
    while i<num:
        if num%i==0:
            sum=sum+i
        i=i+1
    if sum==num:
        print(num,end='  ')
    num=num+1


4.Write a python program for given pattern.
Input:5
Output:
* * * * *
* * * *
* * *
* *
*

n=int(input("enter a number:"))
for i in range(n,0,-1):
    for j in range(i):
        print('*',end=' ')
    print()


5. Write a python program for given pattern.
Input:5
Output:
    *
   **
  ***
 ****
*****'''
n=int(input("Enter a number:"))
for i in range(1,n+1):
    for j in range(n-i):
        print('*',end=' ')
    print()



    
            

