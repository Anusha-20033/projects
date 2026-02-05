'''1)Remove characters that are not alphabets
Input: "abc123@#" 
Output: "abc"

str='abc123@#'
str1='123@#'
remove_special=[]
for i in str:
    if i not in str1:
        print(i,end='')

2)Find first non-repeating character
Input: "swiss" 
Output: "w"

str='swiss'
for i in str:
    if str.count(i)==1:
        print(i)
        break
        
3)Reverse words in a sentence
"I love Python" → "Python love I"

str='I Love Python'
str1=str.split()
str2=str1[::-1]
str3=' '.join(str2)
print(str3,end=' ')


str='I Love Python'
reversed_sentence=' '.join(str.split()[::-1])
print(reversed_sentence)


4)Count occurrences of a character
Input: "banana", 'a' → Output: 3

str="banana"
count=0
for i in str:
    if i=='a':
        count=count+1
print(count)
        

Print characters at even & odd index
Input:s = "python"
Output:Even index characters: p t o
Odd index characters: y h n

s="python"
print("Even index Charcter:",end=' ')
for i in range(len(s)):
    if i%2==0:
        print(s[i],end=' ')
print()
print("odd index Character:",end=' ')
for i in range(len(s)):
    if i%2!=0:
        print(s[i],end=' ')
print()

s="python"
res=s[0:5:2]
res1=s[1:6:2]
print("Even index character:",res)
print("Odd index Character:",res1)


6)Concatenate two strings without using + operator
 Input:s1 = "Hello"       s2 = "World"
Output:HelloWorld
               
s1="Hello"
s2="World"
s3=''.join([s1,s2])
print(s3)

7)Count digits, letters & special characters
Input:s = "abc123@"
Output:Letters = 3
Digits = 3
Special Characters = 1

s="abc123@"
letters=0
digits=0
special=0
for i in s:
    if i.isalpha():
        letters+=1
    elif i.isdigit():
        digits+=1
    else:
        special+=1
print("letters:",letters)
print("digits:",digits)
print("special:",special)


8)Find longest word in a sentence
Input:sentence = "Python is amazing"
     Output:amazing

sentence="Python is amazing"
res=sentence.split()
res1=max(res,key=len)
print(res1)

word="python is amazing".split()
longest=""
for i in word:
    if len(i)>len(longest):
        longest=i
print(longest)'''




