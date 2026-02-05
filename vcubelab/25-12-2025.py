'''itertators
===========
x=[10,20,'vube',50,'true']
for i in x:
    print(i)

x=[10,20,'vube',50,'true']
for i in enumerate(x):
    print(i)

x=[10,20,'vube',50,'true']
for k,v in enumerate(x):
    print(k,v)
    if k==2:
        break
print('*'*30)
for k,v in enumerate(x):
    print(k,v)

x=[10,20,'vube',50,'true']
it=iter(x)
for k,v in enumerate(it):
    print(k,v)
    if k==2:
        break
print('*'*20)
for k,v in enumerate(it):
    print(k,v)

primenumber in recursive function
======================================
def is_prime(num,d=2):
    if num%d==0:
        return False
    elif d<num//2:
        return is_prime(num,d+1)
    else:
        return True
res=is_prime(13)
print(res)

flatten
==========
x=[[1,2],[3,4[5,6,]],7,8]

output=[]
def flatten(y):
    for i in y:
        if type(i)==list:
            flatten(i)
        else:
            output.append(i)
            
x=[[1,2],[3,4],[6,7]]
flatten(x)
print(output)

factorial of number
=====================
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)

res=fact(5)
print(res)

i/p:5
o/p:54321012345
=================
def display(num):
    print(num,end='')
    if num==0:
        return
    display(num-1)
    print(num,end='')
display(5)

1.Find the longest word present in a given sentence.
Input:"Python is a powerful"
Output:"powerful"
st="python is a powerful".split()
longest=""
for i in st:
    if len(i)>len(longest):
        longest=i
print(longest)

3.Write a python Count frequency of prime numbers
in a list. 
Input : arr = [2,2,3,4,5,5,5] 
output : {2:2, 3:1, 5:3}

arr=[2,2,3,4,5,5,5]
output={}
for num in arr:
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            output[num]=output.get(num,0)+1
print(output)

6.Write a recursive function to multiply all digits of a number.
Input: 1234
Output: 24
Explanation: 1 × 2 × 3 × 4 = 24
def multiply(n):
    if n==0:
        return 1
    return (n%10)*multiply(n//10)
res=multiply(1234)
print(res)

5. Move All Zeroes to End 
Input:
arr = [0, 1, 0, 3, 12]
Output:
[1, 3, 12, 0, 0]

arr=[0,1,0,3,12]
arr=arr[1::2]+arr[-1::-2]
print(arr)

7.Write a lambda function to convert a string
to uppercase.
input:text = "hello world"
output:HELLO WORLD

str=lambda x:x.upper()
print(str("hello world"))

8.Write a Python program to extract even
numbers from a list using filter() and a
lambda function.
 Input: [1, 2, 3, 4, 5, 6]
 Output: [2, 4, 6]
 
even=list(filter(lambda x:x%2==0,[1, 2, 3, 4, 5, 6]))
print(even)

Write a Python program to convert a list of
strings to uppercase using map() and a lambda function.
 Input: ["hello", "world"]
 Output: ["HELLO", "WORLD"]

list=list(map(lambda x:x.upper(),["hello", "world"]))
print(list)

5.Write a recursive function to print the nth
term of the Fibonacci series.
Input: 7 terms
Output: 0 1 1 2 3 5 8

def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)

n=7
for i in range(n):
    print(fib(i),end=' ')

count frequency of str
======================
str="banana"
output={}
for i in str:
    output[i]=output.get(i,0)+1
print(output)



