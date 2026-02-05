'''1.Write a program to add a new element to a set.
Input: {1, 2, 3}, element: 4
Output: {1, 2, 3, 4}

s={1,2,3}
element=4
s.add(element)
print(s)


2.Write a program to remove an element from a set
if present.
Input: {1, 2, 3}, element: 2
Output: {1, 3}

s={1,2,3}
s.remove(2)
print(s)

3.Write a program to find the length of a set.
Input: {1, 2, 3, 4}
Output: 4

set={1,2,3,4}
res=len(set)
print(res)

4.Write a program to check if an element exists in a set.
Input: {1, 2, 3}, element: 2
Output: True

s={1,2,3}
element=2
for element in s:
    print("True")
    break

5.Write a program to clear all elements of a set.
Input: {1, 2, 3}
Output: set()

s={1,2,3}
s.clear()
print(s)

6.Write a program to check if two sets are equal.
Input: {1, 2, 3}, {3, 2, 1}
Output: True

s={1,2,3}
s1={3,2,1}
if len(s)==len(s1):
    print("True")

7.Find the union of two sets.
Input: {1, 2}, {2, 3}
Output: {1, 2, 3}

s={1,2}
s1={2,3}
res=s|s1
print(res)

8.Find the intersection of two sets.
Input: {1, 2, 3}, {2, 3, 4}
Output: {2, 3}

s={1,2,3}
s1={2,3,4}
res=s&s1
print(res)


9.Find the difference between two sets.
Input: {1, 2, 3}, {2, 4}
Output: {1, 3}

s={1,2,3}
s1={2,4}
res=s-s1
print(res)


10.Find the symmetric difference between two sets.
Input: {1, 2, 3}, {3, 4, 5}
Output: {1, 2, 4, 5}

s={1,2,3}
s1={3,4,5}
res=s^s1
print(res)'''




    

