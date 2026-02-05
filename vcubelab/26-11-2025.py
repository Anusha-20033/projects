'''1.Write a Python function to find the largest even
number
in a list of integers.
input:List: [12, 5, 7, 8, 4, 19]
output:Largest even number: 12

def largest_even(num):
    evens=[]
    for i in num:
        if i%2==0:
            evens.append(i)
    return max(evens)
List=[12,5,7,8,4,19]
res=largest_even(List)
print("Largest even number:",res)



2.Write a Python function to check whether a number
is a perfect number.
Input:6
Divisors:-1,2,3(1+2+3=6)
          output:True


def perfect_number(num):
    sum=0
    for i in range(1,num+1):
        if i%num==0:
            sum=sum+i
    return sum==num
nums=int(input("Enter a number:"))
res=perfect_number(nums)
print(res)



3.Write a Python function that repeatedly adds
the digits of a number until a single-digit number
is obtained.
input:Enter a number: 9875
output:Final single-digit sum is: 2

def single_digit(nums):
    while nums>9:
        sum=0
        while nums>0:
            sum+=nums%10
            nums//=10
        nums=sum
    return nums
nums=int(input("Enter a number:"))
res=single_digit(nums)
print("Final single-digit sum is:",res)


4.Write a Python function to find the second largest
element in a list.
Enter list: [10, 20, 4, 45, 99]
output:Second largest element is: 45


def second_largest_element(list):
    first=float('-inf')
    second=float('-inf')
    for i in list:
        if i>first:
            second=first
            first=i
        if i>second and i<first:
            second=i
    return second
list=[10,20,4,45,99]
res=second_largest_element(list)
print("Second largest element is :",res)


7.Write a Python function that returns all unique
pairs of numbers from a list that
sum up to a given target.
input:List: [1, 3, 2, 2, 4, 0, 5], Target: 4
output:Pairs that sum to 4: [(1, 3), (2, 2), (4, 0)]

def sum_of_target(list):
    for i in range(0,len(list)):
        for j in range(i+1,len(list)):
            if list[i]+list[j]==target:
                print((list[i],list[j]))
target=int(input("Enter a target value:"))
list=[1,3,2,2,4,0,5]
sum_of_target(list)


8.Write a Python function to print the first n terms
of the Fibonacci series.
input:Enter n: 6
output:Fibonacci Series: 0 1 1 2 3 5


def Fibonacci_series(num):
    a=0
    b=1
    print(a,b,end=" ")
    for i in range(2,nums):
        c=a+b
        print(c,end=" ")
        a=b
        b=c
nums=int(input("Enter a number:"))
Fibonacci_series(nums)'''









          


    


