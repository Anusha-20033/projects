'''case study
============
2.Write a python program to find and return all
substrings of a strings of a string that are palindroms.
i/p:"madam"
o/p:['m','a','d','a','m','ada','madam']

st="madam"
dict={st[i:j] for i in range(0,len(st)) for j in range(i+1,len(st)+1)}
print(dict)

4.WAPP to find the key with the minimum and maximum value in a dictionary.
i/p:{'a':3,'b':1,'c':2}
o/p:min='b',max='a'  

dict={'a':3,'b':1,'c':2}
res=min(dict.())
print(res)

2.Write a Python program to add a new key-value pair
to a dictionary.
Input:
d = {'a': 1, 'b': 2}
Add: c = 3
Output:{'a': 1, 'b': 2, 'c': 3}
d={'a':1,'b':2}
d1={**d,'c':3}
print(d1)

d = {'a': 1, 'b': 2}
d.setdefault('c',3)
print(d)

3.Write a Python program to remove all keys that have duplicate values in the dictionary.
Input:d = {'a': 10, 'b': 20, 'c': 10, 'd': 30}
Output:{'b': 20, 'd': 30}

d = {'a': 10, 'b': 20, 'c': 10, 'd': 30}
output={}
for k,v in d.items:
    for v not in output:
        

    

1.Write a Python program to find the key with the maximum value in a dictionary.
Input:
marks = {'ram': 50, 'sam': 80, 'john': 65}
Output:'sam' 

marks = {'ram': 50, 'sam': 80, 'john': 65}
res=max(marks.keys())
print(res)


4.write a Python program to find all common keys between
two dictionaries.
Input:
d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'b': 20, 'c': 30, 'd': 40}
Output:
['b', 'c']

d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'b': 20, 'c': 30, 'd': 40}
dict=list(d1.keys() & d2.keys())
print(dict)


5.Write a Python program to sort a dictionary in
ascending order based on its values.
Input:
d = {'apple': 3, 'banana': 1, 'mango': 2}
Output:
{'banana': 1, 'mango': 2, 'apple': 3}

d = {'apple': 3, 'banana': 1, 'mango': 2}
dict=list(d.items())
for i in range(0,len(dict)):
    for j in  range(i+1,len(dict)):
        if dict[i][1]>dict[j][1]:
            dict[i],dict[j]=dict[j],dict[i]
dict={key:value for key,value in dict}
print(dict)
               

6.Write a Python program to create a dictionary where each index is mapped to the character at that position in the string.
Input:
s = "ABC"
Output:
{0: 'A', 1: 'B', 2: 'C'}

values="ABC"
keys=[0,1,2]
result={}
i=0
while i<len(values) and i<len(keys):
    result[keys[i]]=values[i]
    i+=1
print(result)


7.Write a Python program to calculate the sum
of all values in a dictionary.
Input:
d = {'a': 10, 'b': 20, 'c': 5}
Output:
35

d = {'a': 10, 'b': 20, 'c': 5}
res=sum(d.values())
print(res)'''

