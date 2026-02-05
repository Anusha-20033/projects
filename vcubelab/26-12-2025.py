'''OOPS
======
class FirstClass:
    def display(self):
        print("anusha")
obj=FirstClass()
obj.display()


class FirstClass:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def addition(self):
        return self.a+self.b
    def multiply(self):
        return self.a*self.b
    def division(self):
        return self.a/self.b
    def subtraction(self):
        return self.a-self.b
    
obj=FirstClass(10,20)
res=obj.addition()
print(res)
res1=obj.multiply()
print(res1)
res2=obj.division()
print(res2)
res3=obj.subtraction()
print(res3)

5.Write a Python program to find the majority element
in a given list of  integers.
A majority element is an element that appears more
than ⌊n/2⌋ times, where n is the length of the list.
Input: nums = [2, 2, 1, 1, 2, 2, 2]
Output: 2
nums=[2,2,1,1,2,2,2]
cnt=0
for i in nums:
    if nums.count(i)>cnt:
        ele=i
        cnt=nums.count(i)
print(ele)

3.Write a Python function to flatten a nested
list into a single list of values using recursion.
input:nested_list = [1, [2, [3, 4], 5], 6]
output:[1, 2, 3, 4, 5, 6]
output=[]
def flatten(y):
    for i in y:
        if type(i)==list:
            flatten(i)
        else:
            output.append(i)
        
x= [1, [2, [3, 4], 5], 6]       
flatten(x)
print(output)

2.Write a recursive function to reverse a string.
Input: "hello"
Output: "olleh"

def string(st):
    output=""
    for i in st:
         output=i+output
    return output
st='hello'
res=string(st)
print(res)

1.Write a recursive function to print numbers
from 1 to n.
Input: n = 5
Output: 1 2 3 4 5
def numbers(n):
    if n>0:
        return n
n=5
for i in range(1,6):
    print(i,end=' ')
numbers(n)

4.Write a recursive function to find the maximum
element in a list.
Input: [1, 4, 2, 9, 5]
Output: 9

def maximum(list):
    if len(list)==0:
        return list[0]
    return max(list[0],maximum(list[1:]))
print(maximum[1,4,2,9,5])
        

 
list=[1,4,2,9,5]
maximum()

6.Given a string, count how many times each character appears in the string and display
the frequency of every character. 
        input : aaabbc 
       output : 3a2bc

class Prime:
    def __init__(self,num):
        self.num=num
    def prime(self):
        for d in range(2,(self.num//2)+1):
            if self.num%d==0:
                return False
            else:
                return True
obj=Prime(13)
res=obj.prime()
print(res)'''


