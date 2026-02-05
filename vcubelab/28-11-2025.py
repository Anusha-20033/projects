'''Find the most frequent character in a string
input:'programming'
output:Most frequent character:'g'
================================================

return common elements
========================
a='programming'
b='gaming'
common=[]
for i in a:
    if i in b:
        common.append(i)
print(common)

5)find lcm of two given number
=================================
num1=int(input("enter a first value:"))
num2=int(input("Enter a second value:"))
if num1>num2:
    small=num1
else:
    small=num2
lcm=0
for i in range(small,(num1*num2)+1):
    if i%num1==0 and i%num2==0:
        lcm=i
print(lcm)


armstrong number or not
==========================
step: read the number
step2:count the digit
step3:take each digit out
step4:find the power of each digit with digit out
step5:sumup all the digit power
step6:compare the sum with armstrong number


num=int(input("Enter a number:"))
d_count=0
sum=0
bkp=num
while num>0:
    num=num//10
    d_count+=1
num=bkp
while num>0:
    t=num%10
    sum=sum+t**d_count
    num=num//10
if sum==bkp:
    print("armstrong")
else:
    print("not armstrong")'''

           
    
