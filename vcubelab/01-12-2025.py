'''1)Write a Program to Reverse given string

x='Anusha'
res=x[::-1]
print(res)

2)Write a Program to Count vowels in the given string
x='anusha'
vowels='aeiou'
count=0
for i in x:
    if i not in vowels:
        count=count+1
print(count)


3)Write a Program to Capitalize First Letter
of Words of given string

x='anusha'
res=x.capitalize()
print(res)

4)Write a Program to Check the given string
Is palindrome or not

str='madam'
if str == str[::-1]:
    print("palindrome")
else:
    print("Not palindrome")

5)Write a Program to Count Occurrence of Substring

str="we are good students are are"
res=str.count("are")
print(res)

6)Write a Program to find the Length of string
x='anusha'
res=len(x)
print(res)

7)Write a Program to Convert to Uppercase
in the given string
str='anusha'
res=str.upper()
print(res)

8)Write a Program to Convert to Lowercase
in the given string
str='ANUSHA'
res=str.lower()
print(res)

9)Write a Program to Concatenate Strings
str1='an'
str2='usha'
res=str1+str2
print(res)

10)Write a Program to Check Character Exists
in the given string or not
str='anusha'
character=input("enter a character :")
if character in str:
    print("character exists")
else:
    print("character is not exists:")'''
