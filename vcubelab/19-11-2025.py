'''1.Using list comprehension, return ASCII values of characters in a string.
Input:
s = "ABC"
Output:
[65, 66, 67]


s="ABC"
x=[ord(i) for i in s]
print(x)


6.Using slicing, rotate the list right by K.
Input:
arr = [10,20,30,40,50]
k = 2
Output:
[40,50,10,20,30]


arr=[10,20,30,40,50]
res=arr[3:]+arr[0:3]
print(res)


7. Rotate the list left by K using slicing.
Input:
arr = [11,22,33,44,55,66]
k = 3
Output:
[44,55,66,11,22,33]


arr=[11,22,33,44,55,66]
res=arr[3:]+arr[0:3]
print(res)



5. Using list comprehension, for each number in the list
return "Prime" or "Not Prime".
Input:
arr = [2, 4, 9, 11, 15]
Output:
['Prime','Not Prime','Not Prime','Prime','Not Prime']'''

arr=[2,4,9,11,15]
x=[prime if arr>0 for i in arr]
print(x)


'''2. Using list comprehension, extract all digits from a string.
Input:
s = "a1b2c3d4"
Output:
['1', '2', '3', '4']

s="a1b2c3d4"
x=[i for i in s if i.isdigit()]
print(x)


3. Using list comprehension, print numbers whose square ends with digit 6.
Input:
arr = [2, 4, 6, 8, 12, 14]
Squares → 4,16,36,64,144,196
Ends with 6 → 16,36,196 → numbers → 4,6,14
Output:
[4, 6, 14]

arr=[2,4,6,12,14]
x=[i for i in arr if (i*i)%10==6]
print(x)

4. Write a program using list comprehension to extract all prime numbers from a given list.
Input:
arr = [10, 3, 5, 12, 17, 19, 20]
Output:
[3, 5, 17, 19]'''

arr=[10,3,5,12,17,19,20]
x=[i if arr>0 for i in arr]





