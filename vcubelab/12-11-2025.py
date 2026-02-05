'''1.Write a python program to print Following pattern.
            Input: 5
            Output:
* * * * *
*       *
*       *
*       *
* * * * *


2.  Write a python program to print digits in Ascending order?
	Input : 4276
	Output: 2467
	
n=list(input("Enter a numbers:"))
output=''.join(sorted(n,reverse=False))
print(output)
	
	
3.Write a python program to print digits in Descending order?
	Input: 3742
	Output: 7432

n=list(input("Enter a number:"))
output=''.join(sorted(n,reverse=True))
print(output)
    
	
4.Write a python program to generate the random 10 numbers to check if those numbers are even or not?
Hint: using the random module 
Write a python program to generate the random 10 number?

import random
for i in range(1,11,2):
        res=random.randrange(i)
        if res%2==0:
            print('even')
        else:
            print('not')
        print(res)       
            

5.Write a Python program to remove duplicate elements from a list.?
    Input:lst = [1, 2, 2, 3, 4, 4]
    Output: [1,2,3,4]

lst=[1,2,2,3,4,4]
duplicate_value=[]
for i in lst:
    if i not in duplicate_value:
        duplicate_value.append(i)
print(duplicate_value)

    
6.Write a Python program to reverse a list without using any built-in functions like reverse() or slicing.?
   input: list: [10, 20, 30, 40, 50]
   Output: list: [50, 40, 30, 20, 10]

list=[10,20,30,40,50]
for i in range(len(list)-1,-1,-1):
    print(list[i],end=' ')

   
7.Write a python program to print Following pattern.
Input: 5
Output:
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *'''
