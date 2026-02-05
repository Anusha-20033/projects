'''1.Slice a list to get the first 3 elements.
List: [10, 20, 30, 40, 50]

list=[10,20,30,40,50]
res=list[0:3:1]
print(res)


2.Slice a list to get elements from index 2 to 4.
List: [1, 2, 3, 4, 5, 6]

list=[1,2,3,4,5,6]
res=list[2:5]
print(res)


3.Slice the list from the 3rd last element to the
last element:
[11, 22, 33, 44, 55, 66]

last_ele=[11,22,33,44,55,66]
res=last_ele[3:]
print(res)


4.Print elements at odd indexes in reverse order.
Input: lst = [10,20,30,40,50,60,70]
Output: [60, 40, 20]


lst=[10,20,30,40,50,60,70]
res=lst[5:0:-2]
print(res)


5.Slice from index 2 to second last in steps of 2
Input: lst = [5,10,15,20,25,30,35,40]
Output: [15, 25, 35]

lst=[5,10,15,20,25,30,35,40]
res=lst[2::2]
print(res)


6.Print middle 4 elements (no len())
Input: lst = [1,2,3,4,5,6,7,8]
Output: [3, 4, 5, 6]

lst=[1,2,3,4,5,6,7,8]
res=lst[2:6:1]
print(res)


7.Reverse list and skip every 2 elements
Input: lst = [1,2,3,4,5,6,7,8,9]
Output: [9, 6, 3]

lst=[1,2,3,4,5,6,7,8,9]
res=lst[8:0:-3]
print(res)


8.Every 3rd element from reverse
Input: lst = [9,8,7,6,5,4,3,2,1]
Output: [1, 4, 7]

lst=[9,8,7,6,5,4,3,2,1]
res=lst[8:0:-3]
print(res)


9.Finding the Maximum Value in a given list by slicing. 
Input: [10,11,12,13,14,15] 
Output:15

lst=[10,11,12,13,14,15]
max_val=lst[0]
for i in lst[1:]:
    if i>max_val:
        max_val=max_val+1
print(max_val)



10.Write a Python program to find the index of
the last occurrence of an element in a list.
input:my_list = [5, 10, 15, 10, 20, 10]
element = 10
output:The last occurrence of 10 is at index: 5

my_list=[5,10,15,10,20,10]
element=10
for i in range(len(my_list)-1,-1,-1):
    if my_list[i]==element:
        print("The occurance of 10 is at index:",i)
        break'''
        









