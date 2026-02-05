'''lamdha functions:
===================
res=lambda x:x**2
r=res(20)
print(r)


res=lambda *args:sum(args)
r=res(10,29,40)
print(r)

1.Write a Python decorator where capital letters
become small, and small letters become capital letter.?
input:"HeLLo PyTHon WorLD"
output:hEllO pYthON wORld
def captial(fun):
    def wraperfun():
        res=fun().swapcase()
        return res
    return wraperfun
@captial
def display():
   st="HeLLo PyTHon WorLD"
   return st
print(display())

2.Write a Python program using a decorator to count the number of words in a sentence returned by a function.?
Input: "Python is very powerful"
 Output: Word count: 4

def count(fun):
    def wraperfun():
        res=fun().split()
        result=len(res)
        return result
    return wraperfun
@count
def display():
    return "Python is very powerful"
print(display())

3.Write a Python program using a decorator to
calculate the ASCII sum of the characters in the
string returned by a function.
Input: "abc"
 Output: ASCII Sum: 294
def decfun(fun):
    def wraperfun():
        res=sum(ord(i)for i in fun())
        return res
    return wraperfun
@decfun
def display():
    return "abc"
print(display())

7.Write a generator to yield even numbers from 1 to n.?
      Input: n = 10
     Output: 2 4 6 8 10

def square(n):
    for i in range(1,11):
        if i%2==0:
            yield i
n=int(input("Enter a number:"))
for n in square(n):
    print(n,end=' ')

5.Write a generator to yield perfect squares from
1 to n.
input:n = 30
output:1 4 9 16 25

def perfectsquare(n):
    for i in range(1,31):
        res=i**2
        yield res
n=int(input("Enter a number:"))
for n in perfectsquare(n):
    print(n,end=" ")

6.Write a generator that yields a sliding
window (of given size k) over a list.
input:List = [1, 2, 3, 4, 5], k = 3
output:[1, 2, 3]  
[2, 3, 4]  
[3, 4, 5]

def sliding(list):
    for i in range(0,len(list)-k+1):
        yield list[i:i +k]
list=[1,2,3,4,5]
k=int(input("Enter a k value:"))
for list in sliding(list):
    print(list,sep=" ")

4.Write a Python program using a decorator to
remove duplicate characters from the returned string.
Input: "aabbccdde"
 Output: abcde
def removeduplicate(fun):
    def wraperfun():
        st=""
        for i in fun():
            if i not in st:
                st=st+i
        print(st)
    return wraperfun
@removeduplicate                      
def display():
    return "aabbccdde"
display()'''

