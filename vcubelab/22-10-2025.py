'''1.Write a Python program to print numbers from n to 1 in reverse order.
 Input: 5
 Output: 5 4 3 2 1

num=int(input("Enter a number:"))
while num>=1:
    print(num)
    num=num-1



2.Write a Python program to find the sum of even numbers from 1 to 50.
Output: 650

num=50
i=1
sum=0
while i<=50:
    if i%2==0:
        sum=sum+i
        i=i+1
print(sum)



3.Write a python program to reverse given number.
Input:123
Output:321

num=int(input("Enter a number:"))
rev=0
while num>0:
    t=num%10
    rev=(rev*10)+t
    num=num//10
print(rev)



4.Write a Python program to check whether a number is a palindrome. 
  Input: 121
 Output: Palindrome

num=int(input("Enter a number:"))
rev=0
temp=num
while num>0:
    t=num%10
    rev=(rev*10)+t
    num=num//10
print(rev)
if temp==rev:
    print("palindrome")
else:
    print("not palindrome")




5.Write a Python program to print the sum of digits of a number.
  Input: 1234
 Output: 10

num=int(input("enter a number:"))
sum=0
while num>0:
    t=num%10
    sum=sum+t
    num=num//10
print(sum)


6.Write a Python program to print the first 10 multiples of a number. Input: 3
 Output: 3 6 9 12 15 18 21 24 27 30

num=int(input("Enter a number:"))
for i in range(1,11):
    print(f"{num*i}",end=' ')



7.Write a Python program to print squares of numbers from 1 to 10.
Output: 1 4 9 16 25 36 49 64 81 100

num=int(input("Enter a number:"))
i=1
while i<=num:
    res=i**2
    i=i+1
    print(res,end=' ')



8.Write a python program to print 1 to n prime numbers.
Input:10
Output:2  3   5  7 

n=int(input("Enter a number:"))
num=2
while num<=10:
    d=2
    while d<=num//2:
        if num%d==0:
            break
        d=d+1
    else:
        print(num,end=' ')
    num=num+1



n=int(input("Enter a number:"))
cnt=0
num=2
while num<=10:
    d=2
    while d<=num//2:
        if num%d==0:
            break
        d=d+1
    else:
        print(num)
        cnt=cnt+1
        if cnt==n:
            break
    num=num+1


n=int(input("Enter a number:"))
cnt=0
num=2
while num<=10:
    d=2
    while d<=num//2:
        if num%d==0:
            break
        d=d+1
    else:
        cnt=cnt+1
        if cnt==n:
            print(num)
            break
    num=num+1'''



    
            



    
    



    
    


 

 


