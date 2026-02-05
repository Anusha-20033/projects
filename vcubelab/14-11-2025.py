'''6.Given a string, slice it to extract the first 3 characters. 
Input:”Vcube” 
Output:” Vcu” 

string="Vcube"
res=string[0:3]
print(res)



7Reversing a List using slicing 
Input: [1,2,3,4] 
Output: [4,3,2,1]

list=[1,2,3,4]
output=list[::-1]
print(output)



8.Write a Python program to rotate a list to the left by k positions.?
input:lst = [1, 2, 3, 4, 5]
        k = 2 
output:Rotated List: [3, 4, 5, 1, 2]

list=[1,2,3,4,5]
output=list[2:]+list[:2]
print(output)



4.Write a Python program to flatten a nested list (list inside another list).
Input: [1, [2, 3], [4, 5]]
Output: [1, 2, 3, 4, 5]

arr=[1,[2,3],[4,5]]
flat_list=[]
for sub_list in arr:
    if type(sub_list)==list:
        for item in sub_list:
            flat_list.append(item)
    else:
        flat_list.append(sub_list)
print(flat_list)



1.Write a Python program to remove all occurrences of a specified value
from a list.?
  Input:lst = [1, 2, 2, 3]
  value = 2
 output:[1, 3]

lst=[1,2,2,3]
value=2
for i in lst:
    if i!=value:
        print(i)


2.Write a Python program to find the index of the first occurrence of an element in a list starting from a given position.
my_list = [5, 10, 15, 10, 20, 10]
element = 10
start_position = 2
output:The index of 10 starting from position 2 is: 3


3.Write a Python program to find all the prime factors of a given number using a function.
Input:  28 
Output: [2, 2, 7]



5.Write a python program to print following pattern.
      N=4

 1  2  3  4
 8  7  6  5
 9 10 11 12
16 15 14 13


even value sum
=================
x=[10,5,15,16,3,2,1]
s=0
for i in range(0,len(x)):
    if i%2==0:
        s=s+x[i]
print(s)


pairs=sum of eual to targets
=============================
x=[1,4,2,5,3,6]
target=int(input("enter a target number:"))
for i in range(0,len(x)):
    for j in range(i+1,len(x)):
        if x[i]+x[j]==target:
            print((x[i],x[j]))'''

