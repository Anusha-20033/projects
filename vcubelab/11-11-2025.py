'''1.Write a Python program to find all the perfect numbers in a given list.?
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




6.Write a python program to print Following pattern.
    *
   * *
  *   *
 *     *
*       *
 *     *
  *   *
   * *
    *

rows=int(input("Enter a row number:"))
space=' '
star='*'
for row_no in range(1,rows+1):
    if 
    


2.Write a python program to find second smallest number in given list
Input: [12,11,11,13,14,16]
Output:12

list=[12,11,11,13,14,16]
first=float('+inf')
second=float('+inf')
for i in list:
    if i<first:
        second=first
        first=i
    if i<second and i>first:
        second=i
print(second)


3.Write a python program to print Following pattern.
    1
   121
  12321
 1234321
123454321


row=int(input("enter a number in rows:"))
space=' '
for i in range(1,row+1):
    print(space*(row-i),end='')
    for j in range(1,i+1):
        print(j,end='')
    for k in range(i-1,0,-1):
        print(k,end='')
    print()







'''5.Write a python program to print Following pattern.
ABCDE
BCDEF
CDEFG
DEFGH
EFGHI
FGHIJ



4.Write a python program to print Following pattern.
    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1'''


