'''using selection sort
=========================
arr=[29,10,14,37,14]
for i in range(0,len(arr)):
    min_value=min(arr[i:])
    idx=arr[i:].index(min_value)+i
    arr[i],arr[idx]=arr[idx],arr[i]
print(arr)


count the elements of distinct elements in a list
===================================================
arr=[1,2,2,3,4,4]
count=0
for i in arr:
    if arr.count(i)>count:
        ele=i
        cnt=arr.count(i)
print(cnt)


2.Write a Python program to find the element that is
repeated the most number of times consecutively in a list.
Input: [10, 1, 1, 1, 1, 1, 2, 2, 2, 2, 1]
Output: 1

x=[10, 1, 1, 1, 1, 1, 2, 2, 2, 2, 1,2,2,2,2,2]
count=0
for i in x:
    if x.count(i)>count:
        ele=i
print(ele)
    



Write a Python program to create a tuple and print it.
 Input: t = (1, 2, 3)
 Output: (1, 2, 3)

t=(1,2,3)
print(t)


4.Write a Python program to access the first
element from a given tuple.
 Input: t = ('apple', 'banana', 'cherry')
 Output: 'apple'

t=('apple', 'banana', 'cherry')
res=t[0]
print(res)


5.Write a Python program to check if a given
element exists in a tuple.
 Input: t = (1, 2, 3, 4), element = 3
 Output: True

t=(1,2,3,4)
res=all(t)
print(res)


6.Write a Python program to concatenate two tuples.
 Input: t1 = (1, 2), t2 = (3, 4)
 Output: (1, 2, 3, 4)

t1=(1,2)
t2=(3,4)
t3=t1+t2
print(t3)


7.Write a Python program to find the index of a
specific element in a tuple.
 Input: t = (10, 20, 30, 40), element = 30
 Output: 2

t=(10, 20, 30, 40)
element = 30
res=t.index(element)
print(res)


8.Write a Python program to count the number of
occurrences of an element in a tuple.
 Input: t = (1, 2, 2, 3), element = 2
 Output: 2

t=(1,2,2,3,3,2)
element=2
count=0
for i in t:
    if t.count(i)>=count:
        ele=i
        count=t.count(i)
print(count)


3.Write a Python program using list comprehension
to find the common elements from two lists.
Input: a = [1, 2, 3, 4], b = [3, 4, 5, 6]  
Output: [3, 4]



1.Write a Python program to shuffle the elements
of a list randomly.
Input:
list = [1, 2, 3, 4, 5]
Sample Output 
Shuffled list: [4, 2, 1, 5, 3]

list=[1,2,3,4,5]
res=(list[3::-2]+list[0::-1])+(list[5::]+list[5:0:-2])
print(res)'''








      



    
    
