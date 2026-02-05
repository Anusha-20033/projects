'''data structures
------------------
list
tuple
set
dictnary

list
=====

list is indicate []
list can stored heterogenous values
list is mutable(can be changed)
stored in ordered manner
allow duplicate values
range start from 0 to n-1

some functions:
append()
remove()


1. Write a Python program using a for loop
to print all perfect cubes between 1 and 100

for i in range(1,5):
    print(i*i*i,end=' ')


2. Write a Python program using a for loop
to print all perfect squares between 1 and 100 ?
for i in range(1,10):
    print(i**2,end=' ')


3. Calculate the LCD of two numbers using a for loop ?

n1=int(input("Enter a n1 number:"))
n2=int(input("Enter a n2 number:"))
if n1>n2:
    small=n1
else:
    small=n2
lcm=0
for i in range(small,(n1*n2)+1):
    if i%n1==0 and i%n2==0:
        lcm=i
print(lcm)


4. Write a Python program to print a right-angled triangle pattern using a for loop.

*
* *
* * *
* * * *
* * * * *

row=int(input("enter a row size:"))
for i in range(1,row+1):
    for j in range(1,i+1):
        print('*',end=' ')
    print()
    
    
5. Write a Python program to calculate the
sum of all elements in a given list.
   Input:[1, 2, 3, 4, 5]
   Output: 15

list=[1,2,3,4,5]
sum=0
for i in list:
    sum=sum+i
print(sum)



6. Write a Python program to count even and odd numbers in a list.
Input:
A list of integers.
List = [1, 2, 3, 4, 5]
Output:
Print the count of even and odd numbers.
Even: 2, Odd: 3


list=[1,2,3,4,5]
even=0
odd=0
for i in list:
    if i%2==0:
        even=even+1
    else:
        odd=odd+1
print("Even:",even , "Odd:",odd)




7.Write a Python program to Find the largest number in a list.?
     Input:[10, 20, 5, 90, 56]
    Output: 90

list=[10,20,5,90,56]
output=list[0]
for list in list[1:]:
    if list>output:
        output=list
print(output)'''




