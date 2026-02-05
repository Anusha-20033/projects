'''1.Return squares of all numbers in the list.
Input:
[1, 2, 3, 4, 5]
Output:
[1, 4, 9, 16, 25]


x=[i**2 for i in [1,2,3,4,5]]
print(x)


2.Extract only even numbers from the list.
Input:
[10, 15, 22, 33, 40]
Output:
[10, 22, 40]

x=[i for i in [10,15,22,33,40] if i%2==0]
print(x)


3.Get lengths of each word in the list.
Input:
["hi", "hello", "python"]
Output:
[2, 5, 6]

x=[len(i) for i in ["hi","hello","python"]]
print(x)


5.Replace each number with its cube.
Input:
[2, 3, 4]
Output:
[8, 27, 64]

x=[i**3 for i in range[2,3,4]]
print(x)


4.Extract only negative numbers.
Input:
[-5, 3, -1, 0, 7, -2]
Output:
[-5, -1, -2]

x=[i for i in [-5,3,-1,0,7,-2] if i<0]
print(x)


7.Replace each number with True if it is even,
else False.
Input:
[3, 6, 8, 11]
Output:
[False, True, True, False]

x=[True if i%2==0 else False for i in [3,6,8,11]]
print(x)


8.Create a list of squares of only odd numbers.
Input:
[1, 2, 3, 4, 5, 6]
Output:
[1, 9, 25]

x=[i**2 for i in [1,2,3,4,5,6] if i%2!=0]
print(x)



9.Extract numbers that are multiples of 3 or 5.
Input:
[3, 7, 10, 12, 14, 15]
Output:
[3, 10, 12, 15]

x=[i for i in [3,7,10,12,14,15] if i%3==0 or i%5==0]
print(x)


6.Extract only those numbers whose sum of digits is even.
Input:
[12, 35, 44, 91, 28]
Output:
[35,91,44, 28]

x=[i for i in [12,35,44,91,28] if sum(int(digit) for digit in str(i))%2==0 ]
print(x)'''







