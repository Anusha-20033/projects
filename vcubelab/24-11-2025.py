'''1.Write a Python program to check if all elements in
a tuple are the same.
 Input: t = (5, 5, 5)
 Output: True

t=(5,5,5)
res=any(t)
print(res)


3.Write a Python program to find the maximum
and minimum elements in a tuple.
 Input: t = (10, 40, 30, 20)
 Output: maximum: 40, minimum: 10

t=(10,40,30,20)
res=max(t)
res1=min(t)
print("maximum:",res)
print("minimun:",res1)


4.Write a Python program to check if a tuple is empty.
 Input: t = ()
 Output: True

t=()
res=all(t)
print(res)


5.Write a Python program to reverse a tuple.
 Input: t = (1, 2, 3)
 Output: (3, 2, 1)

t=(1,2,3)
res=t[::-1]
print(res)


6.Write a Python program to find the index of the
first and last occurrence of a specific element
in a tuple.
 Input: t = (1, 2, 3, 2, 4, 2), element = 2
 Output: First index: 1, Last index: 5

t = (1, 2, 3, 2, 4, 2)
element = 2
first=t.index(element)
last=len(t)-1-t[::-1].index(element)
print("first index:",first)
print("Last index:",last)


7.Write a Python program to repeat the elements
of a tuple n times.
Input: t = (1, 2), n = 3
Output: (1, 2, 1, 2, 1, 2)

t=(1,2)
n=int(input("enter a number:"))
res=t*n
print(res)


8.Write a Python program to remove a specific
element from a tuple.
Input: t = (1, 2, 3, 2), element = 2
Output: (1, 3)

t=(1,2,3,2)
element=2
for i in t:
    if i!=element:
        print(i,end=" ")


9.Write a Python program to multiply all
elements of a tuple.
 Input: t = (2, 3, 4)
 Output: 24

t=(2,3,4)
multi=1
for i in t:
    multi=multi*i
print(multi)

10.Write a Python program to remove duplicate
elements from a tuple.
 Input: t = (1, 2, 2, 3)
 Output: (1, 2, 3) 

t=(1,2,2,3)
output=[]
for i in t:
    if i not in output:
        output.append(i)
output=tuple(output)
print(output)


weekly test paper(22-11-2025)
===============================
#reverse digit in the inside of list
========================================
list=[11,21,31,41,51]
rev=[]
for i in list:
    res=int(str(i)[::-1])
    rev.append(res)
print(rev)


#find the indexs of the multiple values
=======================================
t = (1, 2, 3, 2, 4, 2)
index=[]
element = 2
for i in range(len(t)):
    if t[i]==2:
        index.append(i)
print(tuple(index))


#misssing the value in list
===============================
x=[1,2,4,5]
n=int(input("Enter the value:"))
for i in range(1,n):
    if i not in x:
        print(i)
        break


=================
t=(1,[2,3],4)
t[1].append(5)
print(t)

====================
t=[1,2,3,4]
t[1:3]=[9,9,9]
print(t)

============================
t=((1,2),(3,4,5),(6,7))
flat=()
for i in t:
    for item in i:
        flat=flat+(item,)
print(flat)'''







