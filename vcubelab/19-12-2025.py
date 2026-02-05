'''1.Write a Python program to find the missing number from a list containing numbers from 1 to n
Sample Input:
list = [55, 56, 58, 59], n = 5
output:Missing number: 57

list=[55,56,58,59]
n=5
expsum=0
sum1=0
start=list[0]
for i in range(start,start+n):
    expsum=expsum+i
for num in list:
    sum1=sum1+num
missingvalue=expsum-sum1
print(missingvalue)

Write a Python program to sort a list of integers by ignoring the signs of the numbers.
Input: [-1, 2, 1, 3, -2, -3]
Output: [-1, 1, 2, -2, 3, -3]

list=[-1,2,1,3,-2,-3]
list.sort(key=abs)
print(list)

3. Write a Python program to find the difference between the maximum and minimum elements in a list.
Input: [10, 20, 5, 8] 
 Output: 15.

num=[10,20,5,8]
maxnum=num[0]
minnum=num[0]
for i in num:
    if i>maxnum:
        maxnum=i
    if i<minnum:
        minnum=i
print(maxnum-minnum)

Write a Python decorator that prints "Function started" before and "Function ended" after a function runs.
output:
Function started
Hello!
Function ended
def defun(fun):
    def wraperfun():
        print("Funstion started")
        fun()
        print("Function ended")
    return wraperfun

@defun
def hello():
    print("Hello")
hello()

.Write a Python decorator that converts the output of a function to lowercase.
input:"ALICE"
Output:alice
def defun(fun):
    def wraperfun():
        output=fun().lower()
        return output
    return wraperfun
@defun
def display():
    return "ALICE"
print(display())

Write a Python program using a decorator to count the number of vowels in the output of a function.
Input: "Decorator Example"
 Output: Vowel count: 7'''
def defun(fun):
    def wraperfun():
        vowels="aeiouAEIOU"
        count=0
        for i in fun():
            if i in vowels:
                count=count+1
        print(count)
    return wraperfun
        
@defun        
def display():
    return "Decorator Example"
display()



