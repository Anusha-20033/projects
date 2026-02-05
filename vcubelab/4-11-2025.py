'''1)find the sum of the digits of a given number until single digits
input:45673
output:7

2)print these
input:5
output:
* * * * *
*       *
*       *
*       *
* * * * *


3)find the nth prime number



1)num=int(input("Enter a number:"))
while True:
    sum=0
    while num>0:
        digits=num%10
        sum=sum+digits
        num=num//10
    if sum>9:
        num=sum
    else:
        print(sum)
        break


num=int(input("Enter a number:"))
count=0
while True:
    d=2
    while d<num//2:
        if num%d==0:
            count=count+1
        num=num//10
    if count==num:
        print(num)

3)
1
12
123
1234
12345


row=int(input("Enter a number of rows:"))
i=1
while i<=row:
    j=1
    while j<=i:
        print(j,end='')

        j=j+1
    print()
    i=i+1


5. Write a python program for given pattern.
Input:5
Output:
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5


row=int(input("enetr a number of rows:"))
i=1
while i<=row:
    j=1
    while j<=i:
        print(i,end='')
        j=j+1
    print()
    i=i+1


4. Write a python program for given pattern.
Input:5
Output:
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15

row=int(input("enetr a number:"))
num=1
i=1
while i<=row:
    j=1
    while j<=i:
        print(num,end=' ')
        num=num+1
        j=j+1
    print()
    i=i+1


5)Write a python program for given pattern.
Input:5
Output:
5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1

row=int(input("enetr a number of rows:"))
i=5
while i>=1:
    j=1
    while j<=i:
        print(i,end='')
        j=j+1
    print()
    i=i-1

2. Write a python program for given pattern.
Input:5
Output:
*       * 
  *   *   
    *     
  *   *   
*       *

row=int(input("Enter a number of rows:"))
i=1
while i<=row:
    j=1
    while j<=row:
        if i==j or i+j==row+1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
        j=j+1
    print()
    i=i+1

1. Write a python program for given pattern.
Input:5
Output:
*****
 *****
*****
 *****
***** '''  

row=int(input("enter a number:"))
star='*'
space=' '
middle=(row//2)+1
i=1
while i<=row:
    if i==1 or i==row or i==middle:
        print(star*(row),sep='')
    else:
        print(space,star*(row),sep='')
    i=i+1
    

