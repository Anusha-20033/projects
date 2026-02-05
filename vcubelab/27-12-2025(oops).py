'''class
object
instance variable
instance method
class variable
class method

2.Return the first character that does not repeat.
Input: "swiss"
Output: w

st="swiss"
for i in st:
   if st.count(i)==1:
       print(i)
       break

7. Create a class PerfectNumber to check whether a number is perfect or not.
Input: 28
Output: 28 is a Perfect Number
class perfect:
    def __init__(self,num):
        self.num=num
    def perfectnumber(self):
        sum=0
        for i in range(2,self.num):
            if self.num%i==0:
                sum=sum+i
                print("perfect number")
                break
        else:
            print("not perfect number")
p=perfect(28)
p.perfectnumber()

6. Create a class Factorial with a method to calculate factorial.
Input: 5
Output: 120

class factorial:
    def __init__(self,num):
        self.num=num
    def factorialnumber(self):
        fact=1
        while self.num>=1:
            fact=fact*self.num
            self.num=self.num-1
        print(fact)
f=factorial(5)
f.factorialnumber()

1. Find the length of the longest substring
without repeating characters.
Input::"abcabcbb"
Output: 3'''

st="abcabcbb"
min_value=0
for i in range(0,len(st)):
    for j in range(




'''3. Write a Python program to find the frequency of
each word in a sentence.
Input:"python is easy and python is powerful"
Output:{'python': 2, 'is': 2, 'easy': 1, 'and': 1,
        'powerful': 1}

st="python is easy and python is powerful".split()
output={}
for i in st:
    output[i]=output.get(i,0)+1
print(output)'''
    
4. Write a Python program to remove the key with
the minimum value from a dictionary.
Input:{'a': 10, 'b': 5, 'c': 15}
Output:{'a': 10, 'c': 15}


       


