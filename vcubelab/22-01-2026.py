'''1. Write a Python program to find the second highest number in a list without using sort().
Input: [10, 5, 20, 8]
Output: 10

list=[10,5,20,8]
first=float('-inf')
second=float('-inf')
for i in list:
    if i>first:
        second=first
        first=i
    if i>second and i<first:
        second=i
print(second)

2. Write a Python program to return an array where each element is the product of all other elements.
Input: [1, 2, 3, 4]
Output: [24, 12, 8, 6]
3. Write a Python program to find common elements in three lists using sets.
Input:
[1, 2, 3, 4]
[2, 3, 5]
[2, 6, 3]
Output:{2, 3}
list=[1, 2, 3, 4]
list2=[2, 3, 5]
list3=[2, 6, 3]
res=set(list)&set(list2)&set(list3)
print(res)

4. Write a Python program to demonstrate union, intersection, difference, and symmetric difference operations on two sets.
Input:
Set1 = {1, 2, 3, 4}           Set2 = {3, 4, 5, 6}
Output:
Union: {1, 2, 3, 4, 5, 6}
Intersection: {3, 4}
Difference: {1, 2}
Symmetric Difference: {1, 2, 5, 6}'''

set1={1,2,3,4}
set2={3,4,5,6}
print("Union:",set1|set2)
print("Intersection:",set1&set2)
print("Difference:",set1-set2)
print("Symmetric Difference:",set1^set2)
