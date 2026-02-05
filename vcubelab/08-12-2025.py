'''1.Find the longest word in a sentence
Input: "Python is a powerful programming language"
Output: "programming"

word="Python is a powerful programming language".split()
longest=""
for i in word:
    if len(i)>=len(longest):
        longest=i
print(longest)

t=(1,2,3,4,5,6)
print("even",end=' ')
for i in range(0,len(t)):
    if i%2==0:
        print(i)
print("odd",end=' ')
for i in range(0,len(t)):
    if i%2!=0:
        print(i)


st="he@l#lo123"
for i in st:
    if i.isalpha():
        print(i,end="")
        


st="swiss"
for i in st:
    if st.count(i)==1:
        print(i)
        break
    
2.Move all zeros to the end of the list (keep order)
Input: [0, 1, 0, 3, 12]
Output: [1, 3, 12, 0, 0]
list=[0,1,0,3,12]
res=list[1:6:2]+list[4::-2]
print(res)

5.Return all unique vowels in a string.
Input: "lavanya"
Output: {'a'}

st="lavanya"
for i in st:
    if i=='a':
        print(i)
        break

6.Check if one set is a subset of another
A = {1, 2}
B = {1, 2, 3, 4}
Output: True

A={1,2}
B={1,2,3,4}
res=A.issubset(B)
print(res)

7.Find common elements between two lists
List1 = [1, 2, 3, 4]
List2 = [3, 4, 5, 6]
Output: {3, 4}

list1=[1,2,3,4]
list2=[3,4,5,6]
res=set(list1)& set(list2)
print(res)
       
4.Rotate a list by k positions (right rotation)
Input: [1,2,3,4,5], k=2
Output: [4,5,1,2,3]

list=[1,2,3,4,5]
output=list[3:]+list[:3]
print(output) 


3.Print all pairs in a list whose sum is equal to K
Input: arr=[1, 4, 45, 6, 10, -8], K=16
Output: (10, 6)

arr=[1,4,45,6,10,-8]
k=int(input("enter the k value"))
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j]==k:
            print((arr[j],arr[i]))

arr=[1,4,45,6,10,-8]
k=int(input("Enter a nnumber:"))
for i in range(0,len(arr)):
    diff=k-arr[i]
    if diff in arr:
        print((arr[i],diff))

anagram
===========
st1="listen"
st2="silent"
print(sorted(st1) == sorted(st2))'''
