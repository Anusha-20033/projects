'''1)Reverse a list in Python
Input:
[1, 2, 3, 4, 5]
Output:
[5, 4, 3, 2, 1]

list=[1,2,3,4,5]
res=list[::-1]
print(res)


2)Remove duplicates from a list in Python
Input:
[1, 2, 2, 3, 4, 4, 5]
Output:
[1, 2, 3, 4, 5]

list=[1,2,2,3,4,4,5]
remove_duplicates=[]
for i in list:
    if i not in remove_duplicates:
        remove_duplicates.append(i)
print(remove_duplicates)


3)Find the maximum and minimum elements in a list
Input:
[10, 25, 5, 40, 15]
Output:
Maximum = 40  
Minimum = 5

list=[10,25,5,40,15]
res=max(list)
res1=min(list)
print("maximum =",res)
print("Minimum =",res1)

4)Sort a list in ascending and descending order
Input:
[7, 2, 9, 1, 5]
Output:
Ascending  →  [1, 2, 5, 7, 9]  
Descending →  [9, 7, 5, 2, 1]

list=[7,2,9,1,5]
res=sorted(list)
res1=sorted(list,reverse=True)
print("Ascending -> ",res)
print("Descending -> ",res1)


5)Write a program to remove all vowels from a
given string.
Input:
"Hello World"
Output:
"Hll Wrld"

str='Hello World'
vowels='aeiouAeiou'
for i in str:
    if i not in vowels:
        print(i,end='')


6)Write a program to check if a string is a
palindrome (ignoring spaces).
Input:
"nurses run"
Output:
Palindrome

str='nur ses run'
space=str.replace(" "," ")
if space==space[::-1]:
    print("Palindrome")
else:
    print("not palindrome")


7)Write a program to count the number of consonants
in a given string.
Input:
"Hello"
Output:
3

str="Hello"
vowels="aeiouAEIOU"
count=0
for i in str:
    if i not in vowels:
        count=count+1
print(count)


8)Write a Python program to remove all spaces
from a given string?
input:’Python is fun’
output:’Pythonisfun’

str="Python is fun"
spaces=str.replace(" ","")
print(spaces)


9)Write a Python program to find the length of a string.
input:’Python Programming’
output:Length of the string: 18

str="Python Programming"
res=len(str)
print("Length of the string:",res)'''



