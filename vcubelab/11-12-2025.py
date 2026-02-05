'''x=[(3,4),(-1,2),(5,0),(4,-2)]
for i in range(0,len(x)):
    for j in range(i+1,len(x)):
        if x[i][1]>x[j][1]:
            x[i],x[j]=x[j],x[i]
print(x)


1.Write a Python program to print all possible substrings of a given string.
Input: abc
output:['a', 'ab', 'abc', 'b', 'bc', 'c']

s="abc"
list={s[i:j] for i in range(0,len(s)) for j in range(i+1,len(s)+1)}
print(list)
                            


2.Write a Python program to create a dictionary of squares using dictionary comprehension.
Input: [1, 2, 3]
Output: {1: 1, 2: 4, 3: 9}
dict={i:i**2 for i in [1,2,3]}
print(dict)


3.Write a Python program to create a dictionary where each word is mapped to its length.
Input:
["apple", "banana", "kiwi"]
Output:
{"apple": 5, "banana": 6, "kiwi": 4}

list=["apple","banana","kiwi"]
dict={i:len(i)for i in list}
print(dict)

4.Write a Python program to create a dictionary where list indices are keys and elements are values.
Input:
['a', 'b', 'c']
Output:
{0: 'a', 1: 'b', 2: 'c'}

values=['a','b','c']
keys=[0,1,2]
result={}
i=0
while i<len(values) and i<len(keys):
    result[keys[i]]=values[i]
    i+=1
print(result)
    


9.Write a Python program to create a dictionary that stores numbers as keys and "odd"/"even" as values using dictionary comprehension.
Input:
[1, 2, 3, 4]
Output:
{1: "odd", 2: "even", 3: "odd", 4: "even"}
list=[1,2,3,4]
dict={i:"even" if i%2==0 else "odd" for i in range(1,len(list)+1)}
print(dict)


6.Write a Python program to create a dictionary that contains only the items whose values are greater than 10.
Input:
{'a': 5, 'b': 20, 'c': 15, 'd': 3}
Output:
{'b': 20, 'c': 15}
dict={'a': 5, 'b': 20, 'c': 15, 'd': 3}
dict1={key:value for key,value in dict.items() if value>10}
print(dict1)

7.Write a Python program to convert a list of tuples into a dictionary using dictionary comprehension.
Input:
[(1, 'a'), (2, 'b'), (3, 'c')]
Output:
{1: 'a', 2: 'b', 3: 'c'}

list=[(1, 'a'), (2, 'b'), (3, 'c')]
dict={key:value for key,value in list}
print(dict)

5.Write a Python program to reverse keys and values using dictionary comprehension.
Input:
{'x': 1, 'y': 2, 'z': 3}
Output:
{1: 'x', 2: 'y', 3: 'z'}

dict={'x': 1, 'y': 2, 'z': 3}
dict1={value:key for key,value in dict.items()}
print(dict1)


8.Write a Python program to create a dictionary where each character of a string is mapped to its ASCII value.
Input:
"ABC"
Output:
{'A': 65, 'B': 66, 'C': 67}

st="ABC"
dict={i:ord(i) for i in st}
print(dict)'''



