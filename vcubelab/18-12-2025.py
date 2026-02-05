'''Generators
===========
1.Move All Zeros to the End (Maintain Order)
Input: [0, 1, 0, 3, 12]
Output: [1, 3, 12, 0, 0]

list=[0,1,0,3,12]
res=list[1:5:2]+list[-1:-6:-2]
print(res)

2.Reverse Words in a Sentence (Characters Same)
Input: "Python is easy"
Output: "easy is Python"

str="python is easy"
res=str.split()
print(' '.join (res[::-1]))


3.Write a Python function to find the longest
common substring between two strings.
input:String 1: abcde
String 2: abfc
output:Longest common substring: ab

str1="abcde"
str2="abfc"
st=""
print(st)

5.Write a Python function to sort a list in ascending order without using built-in sort functions and slicing.
input:List: [3, 1, 4, 2, 5]
output:Sorted list: [1, 2, 3, 4, 5]

list=[3,1,4,2,5]
for i in range(0,len(list)):
    for j in range(i+1,len(list)):
        if list[i]>list[j]:
            list[i],list[j]=list[j],list[i]
print(list)


4.Write a Python function to find the largest even number in a list of integers.
input:List: [12, 5, 7, 8, 4, 19]
output:Largest even number: 12

def largestevennumber(list):
    largest=0
    for i in list:
        if i%2==0:
            if i>largest:
                largest=i
    return largest 
    
list=[5,7,8,4,12,19]
print(largestevennumber(list))

6. Write a Python generator function to yield
Fibonacci numbers up to n terms.
input:n = 6
output:0 1 1 2 3 5

def gen(n):
    a=0
    b=1
    for i in range(n):
        yield a
        c=a+b
        a=b
        b=c
n=int(input("Enter a number:"))
for n in gen(n):
    print(n,end=' ')

        
7. Write a generator that yields all prime numbers
up to a given number n.
input:n = 10
output:2 3 5 7


def prime(n):
    for i in range(2,n+1):
        is_prime=True
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                is_prime=False
                break
        if is_prime:
                yield i
n=int(input("Enter a number"))
for p in prime(n):
    print(p,end=' ')


8. Write a generator function to yield only vowels
from a string.
input:string = "education"
output:e u a i o

str="education"
vowels="aeiouAEIOU"
st=[]
for i in str:
    if i in vowels:
        st.append(i)
        print(i,end=' ')


def string(st):
    vowels="aeiouAEIOU"
    for i in st:
        if i in vowels:
            yield i
st="education"
for i in string(st):
    print(i,end=' ')'''
