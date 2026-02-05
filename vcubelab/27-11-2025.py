'''1)Write a program to count how many characters are in a given string, including spaces?
Input:’Hello World’
output:Number of characters: 11

a='Hello world'
count=len(a)
print("Number of Character:",count)


2)Write a program to count how many characters are in
a given string, but do not count spaces?
input:’Hello World’
output:Number of characters (excluding spaces): 10

a='Hello World'
count=len(a)-1
print("Number of Character:",count)

a='Hello world'
count=len(a.replace(" ",""))
print("Number of Characters(excluding spaces):",count)

3)Write a Python program to convert all lowercase
letters in a string to uppercase?
input:’welcome to python’
output:’WELCOME TO PYTHON’

a="'welcome to python'"
upper=a.upper()
print(upper)


4)Write a Python program to convert all capital letters in a string to small letters?
input:’ HELLO WORLD’
output:’hello world’

x="'HELLO WORLD'"
lower=x.lower()
print(lower)


10)Write a Python program to reverse a given string?
input:Python
output:nohtyP


x='Python'
reverse=x[::-1]
print(reverse)


5)Write a Python program to print only the vowels from a given string?
input:’Programming is fun’
output:’o a i i u’


x="'Programming is fun'"
vowels="'aeiou'"
for i in x:
    if i in vowels:
        print(i,end=" ")


6).Write a Python program to print only the consonants from a given string?
input:’Python is cool’
output: ‘P y t h n s c l’

x="'Python is cool'"
vowels="'aeiou'"
for i in x:
    if i not in vowels:
        print(i,end=" ")


7)Write a Python program to count how many vowels
are in a given string?
input:’Education is important’
output: 9

x="'education is important'"
vowels="aeiouAEIOU"
count=0
for i in x:
    if i in vowels:
        count=count+1
print("Number of Vowels:",count)


8).Write a Python program to count how many
consonants are in a given string?
input:’Hello World’
output:Number of consonants: 7

x='Hello World'
vowels="aeiouAEIOU"
count=0
for i in x:
    if i.isalpha() and i not in vowels:
        count=count+1
print("Number of Consonants:",count)



9).Write a Python program to count how many vowels
and consonants are in a given string?
input: ‘Welcome to Python’
output:Number of vowels: 5  
Number of consonants: 10'''


x='Welcome to python'
vowels_count=0
conso_count=0
vowels="aeiouAEIOU"
for i in x:
    if i.isalpha():
        if i in vowels:
            vowels_count+=1
        else:
            conso_count+=1
print("Number of Vowels:",vowels_count)
print("Number of consonants:",conso_count)
       







