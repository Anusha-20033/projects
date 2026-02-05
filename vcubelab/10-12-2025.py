'''convert decimal to Roman number
=================================

dtor={40:'L',10:'X',9:'IX',5:'v',4:'IX',1:'I'}
num=int(input("Enter number to convert:"))
output=''
for k in dtor:
    q=num//k
    if q>0:
        output=output+q*dtor.get(k)
        num=num%k
print(output)

Dictinanary
===============
x={'a':20,3:'anu','c':56}
res=list(x.keys())
res=list(x.values())
res=list(x.items())
print(res)


2.Write a Python program to create a dictionary from
two lists.
Input: keys = ['a', 'b', 'c'], values = [1, 2, 3]
Output: {'a': 1, 'b': 2, 'c': 3}

keys=['a','b','c']
values=[1,2,3]
result={}
i=0
while i<len(keys) and i<len(values):
    result[keys[i]]=values[i]
    i+=1
print(result)

keys=['a','b','c']
values=[1,2,3]
result={}
for i in range(min(len(keys),len(values))):
    result[keys[i]]=values[i]
print(result)

3.Write a Python program to check if a key exists
in a dictionary.
Input:  {'a': 1, 'b': 2}
key=’a’
Output: True

dict={'a':1,'b':2}
key='a'
if dict!=key:
    print('True')


4.Find sum of positive numbers
Input: [1,-2,3,4]
Output: 8

list=[1,-2,3,4]
sum=0
for i in list:
    if i>0:
        sum=sum+i
print(sum)

    
5.Check if two lists are equal
Input: [1,2,3] & [1,2,3]
Output: True

list1=[1,2,3]
list2=[1,2,3]
if list1==list2:
    print('True')


6.Remove a specific element
Input: [1,2,3,2], remove 2
Output: [1,3,2]

list=[1,2,3,2]
output=[]
for i in list:
    if i not in output:
        output.append(i)
print(output)


1.Write a Python program to convert a given number
into words.
Input:123
Output:one hundred twenty three'''
dton={1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',
10:'ten',11:'elven',12:'twelve',20:'twenty',100:'hundred'}
num=int(input("enter a number:"))
output=''
for i in dton:
    t=num//i
    if 
print(output)

    
