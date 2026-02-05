'''1)Remove duplicates from a list in Python
Input:
[1, 2, 2, 3, 4, 4, 5]
Output:
[1, 2, 3, 4, 5]

list=[1, 2, 2, 3, 4, 4, 5]
output=[]
for i in list:
    if i not in output:
        output.append(i)
print(output)
2)Find the maximum and minimum elements in a list
Input:
[10, 25, 5, 40, 15]
Output:
Maximum = 40  
Minimum = 5
list=[10, 25, 5, 40, 15]
print("Maximim:",max(list))
print("Minimun:",min(list))


3)Sort a list in ascending and descending order
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

4)Write a program to remove all vowels from a given string.
Input:
"Hello World"
Output:
"Hll Wrld"
str="Hello World"
vowels="aeiouAEIOU"
for i in str:
    if i not in vowels:
        print(i,end='')

5)Write a program to check if a string is a palindrome (ignoring spaces).
Input:
"nur ses run"
Output:
Palindrome

str='nur ses run'
space=str.replace(" "," ")
if space==space[::-1]:
    print("Palindrome")
else:
    print("not palindrome")
    
6)	Write a Python program to remove all spaces from a given string?
input:’Python is fun’
output:’Pythonisfun’
str="Python is fun"
res=str.replace(" ","")
print(res)

7)Write a Python program to find the length of a string.
input:’Python Programming’
output:Length of the string: 18'''
str="Python Programming"
res=len(str)
print("Length of the string:",res)
