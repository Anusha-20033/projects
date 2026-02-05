'''word frequency and line count
===============================
st='hyderadad is the capital city of TG and hyderabad is the financial district and beautiful'
output={}
for i in st:
    if len(i)<len(st):
        output[len(i)]=output.get(i,0)+1
        output=i
print(output)

frequency of the character
=============================
st='anusha'
output={}
for i in st:
    output[i]=output.get(i,0)+1
print(output)

list=[1,2,3,4,5,6]
target=7
for i in range(0,len(list)-1):
    diff=target-list[i]
    if diff in list:
        print((list[i],diff))
        

list=[2,2,5,4,1,5,1,9,4,1,0]
output=[]
for i in list:
    if i not in output:
        output.append(i)
print(output)


def is_palindrome(st):
    if st==st[::-1]:
        return 'True'
    else:
        return 'False'
st='racecar'
res=is_palindrome(st)
print(res)

without using built-in functions
==================================
st="hello"
output=""
for i in st:
    output=i+output
print(output)'''
a=5
b=10
a,b=b,a
print("b",b)
print("a",a)


       
