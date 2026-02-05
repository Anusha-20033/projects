'''1.Write a Python function to check whether a
given number is even or odd.
input:Enter a number: 7
Output:odd


def even_odd(num):
    if num%2==0:
        return 'even'
    else:
        return 'odd'
num=int(input("enter a number:"))
res=even_odd(num)
print(res)


2.Write a Python function to find the
square of a given number.
input:Enter a number: 7
Output:49

def square(num):
    t=num**2
    return t
num=int(input("enter a number:"))
res=square(num)
print(res)


5.Write a Python function to check if a given
number is a palindrome.
input:Enter a number: 121
Output:palindrome

def palindrome(num):
    rev=0
    temp=num
    while num>0:
        t=num%10
        rev=(rev*10)+t
        num=num//10
    if temp==rev:
        print('palindrome')
    else:
        print('not palindrome')
    
num=int(input("Enter a number:"))
palindrome(num)




def is_palindrome(num):
    if str(num)==str(num)[::-1]:
        print("palidrome")
    else:
        print("not palindrome")
num=int(input("enter a number:"))
is_palindrome(num)



3.Write a Python function to check whether a
given number is a perfect square.
input:Enter a number: 49
output:49 is a perfect square.

def perfect_square(num):
    root=int(num**0.5)
    if root*root==num:
        print(f"{num} is a perfect square")
    else:
        print(f"{num} is not a perfect square")
num=int(input("Enter a number:"))
perfect_square(num)

        
4.Write a Python function to check whether a given
number is a perfect cube. input:Enter a number: 27
output:27 is a perfect cube. 

def perfect_cube(num):
    root=round(num**(1/3))
    if root**3==num:
        print(f"{num} is a perfect cube")
    else:
        print(f"{num} is not a perfect cube")
num=int(input("Enter a number:"))
perfect_cube(num)
        

6).Write a Python function to find the smallest
digit in a given number.
input:Enter a number: 38249
Output:2

def smallest_digit(num):
    small=100
    while num>0:
        t=num%10
        if t<small:
            small=t
        num=num//10
    return small
num=int(input("Enter a number:"))
res=smallest_digit(num)
print(res)


9).Write a Python function to calculate the sum
of even digits in a number.
input:Enter a number: 123456
Output:Sum of even digits: 12


def sum_of_even_digit(num):
    even=0
    for i in str(num):
        if int(i)%2==0:
            even=even+int(i)
    print("Sum of even digits:",even)
num=int(input("enter a number:"))
sum_of_even_digit(num)


7.Write a Python function to find the product
of all digits in a number.
Input:Enter a number: 123
output:Product of digits is 6
def product_of_digit(num):
    multi=1
    for i in str(num):
        multi=multi*int(i)
    print(multi)
num=int(input("enter a number:"))
product_of_digit(num)


10).Write a Python function to count the number of
factors of a given number.
Input:Enter a number: 12
output:Number of factors of 12 is 6

def count_factors(num):
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count=count+1
    print(count)
num=int(input("Enter a number:"))
count_factors(num)'''












