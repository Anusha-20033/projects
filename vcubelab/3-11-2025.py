'''4)Write a Python program to print the digits of a number in descending order using a while loop.
Input:Enter a number: 4276
Output:7642

num=list(input("Enter a number:"))
output=''.join(sorted(num,reverse=True))
print(output)



2.Write a Python program to print a square star pattern based on the number of rows entered by the user.
Input:Enter the row size: 4
Output:
* * * *
* * * *
* * * *
* * * *


rows=int(input("enter the row size:"))
i=1
while i<=rows:
    j=1
    while j<=rows:
        print('*',end=' ')
        j=j+1
    print()
    i=i+1



Write a Python program to print the digits of a number in ascending  order using a while loop.
Input:Enter a number: 4276
Output:2467

num=list(input("Enter a number:"))
output=''.join(sorted(num))
print(output)'''










