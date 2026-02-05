'''1.Write a python program to Find  Pairs With Given Sum.
Input:([1,2,3,4,5]      target=6)
Output:[(1,5),(2,4)]

x=[1,2,3,4,5]
target=int(input("Enter a target value:"))
for i in range(0,len(x)):
    for j in range(i+1,len(x)):
        if x[i]+x[j]==target:
            print([(x[i],x[j])],end="")



4.Find the First Repeating Element in an List
Input:
arr = [10, 5, 3, 4, 3, 5, 6]
Output:
5

arr=[10,5,3,4,3,5,6]
for i in arr:
    if i==5:
        print(i)
        break
    
7.Move Negative Numbers to Left 
Input:
arr = [-1, 2, -3, 4, -5]
Output:
[-1,-3, -5, 4, 2]


arr=[-1,2,-3,4,-5]
res=arr[0::2]+arr[1::2]
print(res)


3.Write a python program to Find All Duplicates.
Input:[1,2,3,2,4,1]
Output:[1,2]

lst=[1,2,3,2,4,1]
output=[]
output1=[]
for i in lst:
    if i in output1 and i not in output:
        output.append(i)
    if i not in output1:
        output1.append(i)
print(output)


5. Move All Zeroes to End 
Input:
arr = [0, 1, 0, 3, 12]
Output:
[1, 3, 12, 0, 0]

arr=[0,1,0,3,12]
arr=arr[1::2]+arr[-1::-2]
print(arr)

    
2. Write a python program to Split List into Chunks of size N.
Input: ( [1,2,3,4,5,6,7]     n=3)
Output:  [[1,2,3],[4,5,6],[7]]

lst=[1,2,3,4,5,6,7]
n=int(input("Enter a size number:"))
chunks=[]
for i in range(0,len(lst),n):
    chunk=lst[i:i+n]
    chunks.append(chunk)
print(chunks)
    
    
6. Find Missing Number from 1 to N 
Input:
arr = [1, 2, 4, 5, 6], n = 6
Output:
3


arr=[1,2,4,5,6]
n=int(input("enetr a number:"))
for i in range(1,n):
    if i not in arr:
        print(i)
        break


x=[1,3,4,52,6,5,7,8]
x.append(4)
print(x)

with out using append function
===============================
x=[1,3,4,2,5,6,7,8]
y=[100]
z=x+y
print(z)

extend()
===========

        
        
