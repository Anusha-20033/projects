'''1.Write a Python program to count the frequency
of each character in a given string using a dictionary.
Input:"programming"
Expected Output:{'p': 1, 'r': 2, 'o': 1, 'g': 2,
                 'a': 1, 'm': 2, 'i': 1, 'n': 1}
st="programming"
output={}
for i in st:
    output[i]=output.get(i,0)+1
print(output)

4. Write a Python program to find all the prime numbers in a given list. 
Input:lst = [1, 2, 3, 4, 5, 10, 13, 15, 17] 
output:[2, 3, 5, 13, 17]

list=[1, 2, 3, 4, 5, 10, 13, 15, 17]
output=[]
i=2
for num in list:
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            output.append(num)
print(output)

5. Write a Python program to find all the strong
numbers in a given list.? 
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
print(strong_number)

Write a Python program to reverse each number
inside a list. 
Input: [11, 21, 31, 41, 51] 
Output: [11, 12, 13, 14, 15]

list=[11, 21, 31, 41, 51]
reversed=[]
for i in list:
    rev=int(str(i)[::-1])
    reversed.append(rev)
print(reversed)

6. Create a class Rectangle that calculates
the area and perimeter of a rectangle.
class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        area=self.length*self.breadth
        return area
    def perimeter(self):
        perimeter=2*(self.length+self.breadth)
        return perimeter
r=Rectangle(2,3)
res=r.area()
print(res)
res1=r.perimeter()
print(res1)

7. Create a class Circle that calculates the
area and circumference of a circle.
area of circle=3.147*r2
circumference=2*3.147*r
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        area=3.147*(self.radius)**2
        return area
    def circumference(self):
        circumference=2*3.147*self.radius
        return circumference
c=Circle(3)
res=c.area()
print(res)
res1=c.circumference()
print(res1)

8. Create a class BankAccount with account_no and balance.
Deposit and withdraw amount based on user input.
Input:
Account No: 12345
InitialBalance: 5000
Deposit Amount: 2000
Withdraw Amount: 1000
Output:Final Balance: 6000'''
class BankAccount:
    def __init__(self,accountno,Balance,Deposit,Withdraw):
        self.accountno=accountno
        self.Balance=Balance
        self.Deposit=Deposit
        self.Withdraw=Withdraw
    def deposit(self):
        self.deposit=self.Balance+self.Deposit
        return self.deposit
    def withdraw(self):
        self.withdraw=self.Deposit-self.Withdraw
        return self.withdraw
    def final(self):
        final=self.deposit-self.withdraw
        return final
b=BankAccount(12345,5000,2000,1000)
res1=b.deposit()
print(res1)
res2=b.withdraw()
print(res2)
res=b.final()
print(res)


