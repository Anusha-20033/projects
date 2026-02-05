'''1)positional paramaters
2)default parameters
3)keywords arguments
4)varable length arguments
  1)list of args
  2)dictionary of keyword args


1)def addition(a,b):#function defination or called
    c=a+b
    return c
res=addition(10,20)#function calling
print(res)


2)def addition(a,b=40):#52
    c=a+b
    return c
res=addition(12)
print(res)

def addition(a=10,b):#error
    c=a+b
    return c
res=addition(12)
print(res)

def addition(a=10,b=50):#60
    c=a+b
    return c
res=addition()
print(res)

def addition(a=70,b=50):#60
    c=a+b
    return c
res=addition(10)
print(res)

3)def info(name,age):
    s=f"""My name is {name} and his/her age is {age}"""
    return s
res=info(34,'anu')
print(res)#My name is 34 and his/her age is anu

def info(name,age):
    s=f"""
My name is {name} and his/her age is {age}
"""
    return s
res=info('anu',23)
print(res)

def info(name,age):
    s=f"""My name is {name} and his/her age is {age}"""
    return s
res=info(age=24,name='anu')
print(res)'''

'''1.Write a Python program to group elements in a
list by their length using a dictionary.
 Input: ['a', 'to', 'cat', 'dog']
  Output: {1: ['a'], 2: ['to'], 3: ['cat', 'dog']}

list=['a','to','cat','dog']


5.Write a Python program to merge two dictionaries
by combining values of common keys.
      Input: {'a': 1, 'b': 2}, {'b': 3, 'c': 4}
     Output: {'a': 1, 'b': 5, 'c': 4}

dict1={'a':1,'b':2}
dict2={'b':3,'c':4}
for i in dict2:
    if i in dict1:
        dict1[i]=dict1[i]+dict2[i]
    else:
        dict1[i]=dict2[i]
print(dict1)
        

6.Write a Python function to calculate the
sum of even digits in a number.
input:Enter a number: 123456
Output:Sum of even digits: 12

def sum_of_even_digits(numbers):
    even=0
    odd=0
    for digit in str(numbers):
        if int(digit)%2==0:
            even=even+int(digit)
        else:
            odd=odd+int(digit)
    return even
numbers=int(input("Enter a number:"))
res=sum_of_even_digits(numbers)
print("Sum of Even digits:",res)

7.Write a Python function to count the number
of factors of a given number.
Input:Enter a number: 12
output:Number of factors of 12 is 6

def factors(num):
    fact=0
    for i in range(1,num+1):
        if num%i==0:
            fact=fact+1
    return fact
num=int(input("Enter a number:"))
res=factors(num)
print("Number of factors of 12 is",res)


8.Write a Python function to count the number of vowels and consonants in a string.
input:Enter a string: Hello World
output:Vowels: 3  
Consonants: 7

def count(x):
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
x='Hello World'
count(x)

       
2.Write a Python program to flatten a tuple of
tuples into a single tuple.
 Input: t = ((1, 2), (3, 4), (5,))
 Output: (1, 2, 3, 4, 5)

t=((1,2),(3,4),(5,))
flat=()
for i in t:
    for item in i:
        flat=flat+(item,)
print(flat)

4.Write a Python program to find the key with the second highest value.
     Input: {'a': 10, 'b': 40, 'c': 30}
    Output: 'c'

dict1={'a': 10, 'b': 40, 'c': 30}



x={'a': 10, 'b': 40, 'c': 30}
y={'c':30,'e':60}
#output={'a': 10, 'b': 40, 'c': 30,'e':60}
x.update(y)
print(x)

x={'a': 10, 'b': 40, 'c': 30}
y={'d':60,'e':60}
#output={'a': 10, 'b': 40, 'c': 30,'d':60,'e':60}
x.update(y)
print(x)


x=['a','b','c','d']
#output={'a':0,'b':0,'c':0,'d':0}
res=dict.fromkeys(x,0)
print(res)


x={'a':1,'b':2,'c':1}
#output={1:[a,c],2:[b]}
output={}
for k in x.keys():
    if x[k] in output:
        output[x[k]].append(k)
    else:
        output[x[k]]=[k]
print(output)


x={'a':1,'b':2,'c':1}
#output={1:[a,c],2:[b]}
output={}
for k,v in x.items():
    if v in output:
        output[v].append(k)
    else:
        output[v]=[k]
print(output)


x={'a': 10, 'b': 50, 'c': 30}
y={'d':30,'b':40,'c':60}
#output={'a': 10, 'b': 90, 'c': 90,'d':30}
for i in y:
    if i in x:
        x[i]=x[i]+y[i]
    else:
        x[i]=y[i]
print(x)

ADD the element without using built-in functions
====================================================
x={'a':10,'b':20,'c':30}
y={**x,'d':100}
print(y)


common functions
================
min,max,sum,sorted,any,all,len

it can applied only on keys
===========================
x={'a': 10, 'b': 50, 'c': 30}
#print(max(x))
#print(min(x))
#print(len(x))
#print(sorted(x))
#print(any(x))
#print(all(x))'''

