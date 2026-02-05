'''num=int(input("Enter a number:"))
i=0
d=1
while d<num:
    if num%d==0:
        i=i+d
    d=d+1
if i==num:
    print(num,"is a perfect number")
else:
    print(num,"is not perfect number")


age=int(input("Enter a age"))
if age <=12:
    print("child")
elif age<=19:
    print("teen")
elif age<=50:
    print("adult")
else:
    print("senior")



num=int(input("enter a number:"))
sum=0
while num>0:
    t=num%10
    sum=sum+t
    num=num//10
print(sum)



n1=int(input("Enter a n1 number:"))
n2=int(input("Enter a n2 number:"))
if n1<n2:
    small=n1
else:
    small=n2
d=1
gcd=0
while d<=small:
    if n1%d==0 and n2%d==0:
        gcd=d
    d=d+1
else:
    if gcd!=0:
        print("gcd",gcd)
    else:
        print("no gcd")


x=100
if x//3:
    print('yes')
else:
    print('no')



n=10
while n:
    n=n//2
print(n)



a=True
b=False
print(a and not b or b)'''






        
    
    




