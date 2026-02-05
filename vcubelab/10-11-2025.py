'''1.Write a Python program to count the number of occurrences of a
specific element in a list.?
    Input :lst = [1, 2, 3, 2, 2, 4]
     element=2
     Output: 3

lst=[1,2,3,2,2,4]
element=2
count=lst.count(element)
print("output:",count)


lst=[1,2,3,2,2,4]
element=2
count=0
for i in lst:
    if i==element:
        count=count+1
print(count)



2.Write a Python program to concatenate two lists without using the built-in extend() method.?
 Input:a = [1, 2, 3]
       b = [4, 5, 6]

a=[1,2,3]
b=[4,5,6]
print(a+b)


8.Write a python program to find second highest number in given list
Input: [12,11,11,13,14,16]
Output:14

list=[12,11,11,13,14,16]
first=float('-inf')
second=float('-inf')
for i in list:
    if i>first:
        second=first
        first=i
    if i>second and i<first:
        second=i
print(second)


4.Write a Python program to check whether a given list is empty or not.
input:my_list = [1, 2, 3]
output:The list is not empty

my_list=[1,2,3]
if len(my_list)==0:
    print("the list is empty")
else:
    print("the list is not empty")


3.Write a Python program to find common elements between two lists.
    Input:a = [1, 2, 3],  b = [2, 3, 4]
     output:[2, 3]
     

a=[1,2,3]
b=[2,3,4]
list=[]
for i in a:
    if i in b:
        list.append(i)
print(list)
    
    
7.Write a Python program to find all the perfect numbers in a given list.?
   Input:lst = [6, 28, 12, 496, 100]
  output:[6, 28, 496]
  
lst=[6,28,12,496,100]
perfect_number=[]
for num in lst:
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum=sum+i
    if sum==num:
        perfect_number.append(num)
        
print(perfect_number)       



5.Write a Python program to find all the prime numbers in a given list.
  Input:lst = [1, 2, 3, 4, 5, 10, 13, 15, 17]
  output:[2, 3, 5, 13, 17]


lst=[1,2,3,4,5,10,13,15,17]
prime_list=[]
for num in lst:
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            prime_list.append(num)
print(prime_list)
        



6.Write a Python program to find all the strong numbers in a given list.?
   Input:lst = [1, 2, 145, 40585, 123] 
 output:[1, 2, 145, 40585]


lst=[1,2,145,40585,123]
strong_number=[]
for num in lst:
    temp=num
    total=0
    while temp>0:
        digit=temp%10
        fact=1
        for i in range(1,digit+1):
            fact=fact*i
        total=total+fact
        temp=temp//10
    if total==num:
        strong_number.append(num)
print(strong_number)'''




