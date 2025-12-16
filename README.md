# Question-for-python-
 
## Password Matching Program
```python
password=input("Enter password")
email=input("Enter mail")

if password=="1234"and email=="majid9911@gmail.com":
    print("Welcome")
else:
    print("Invalid password")
```

## Find Maximum Program
```python
a =int(input("enter number"))
b =int(input("enter number"))
c =int(input("enter number"))
max=a
if a>b:
    if a>c:
        max=a
    else:
        if c>b:
            max=c
else:
    if b>c:
        max=b
    else:
        max=c  
print(max)  
```

## Sum of Series Program
```python
# 1+1/1!+2/2!+3/3!...
res=0
f=1       
for i in range(1,2):
    f=f*i
    res=res+i/f

print(res)
for i in range(1,6):
    for j in range(1,6):
        print('*',end="")
    print()
```

## Number Pyramid Program
```python
#1
#1 2 1
#1 2 3 2 1
#1 2 3 4 3 2 1
for i in range(1,6):
    for j in range(1,i+1):
        print(j, end=' ')
    for k in range(i-1,0,-1):
        print(k,end=' ')
    print()
```

## Prime Numbers
```python
for i in range(10,100):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)
```

## Count Character
```python
s = 'Majid'
fre=0
for i in s:
    if i=='i': fre=fre+1
print(fre)
```

## Vowel or Constant
```python
s ="aeiou"
for i in s:
    if i=='e' or i=='i'or i=='a'or i=='o'or i=='u':
        print(i,"is vowel")
    else:
        print(i,'not a vowel')
```

## Fibonacci Series
```python
pre=0
curr=1
print(0,1,end=" ")

for i in range(3,10):
    res=pre+curr
    print(res,end=" ")
    pre=curr
    curr=res
```

## Bill Calculation
```python
units = int(input("enter consumed units"))
p_perUnit=int(input("Enter prince of one units"))
```

## List Sum
```python
list =[1,2,3,4,5,6]
sum=0

for i in list:
    sum+=i
print(sum)
```

## Leap Year
```python
year = int(input("enter year "))
if (year%4 and year%100!=0) or year%400 :
    print(year," is leap year")
else:
    print("Not a leap year")
```

## Basic Programs to Understand Functions

### Print a Given List
```python
def sum(list):
    for i in list:
        print(i)
```

### Reverse a List Using Two Pointers
```python
def reverse(list):
    j = len(list)-1
    i=0
    while i<j:
       temp = list[i]
       list[i]=list[j]
       list[j]=temp
       i+=1
       j-=1
    for i in list:
        print(i, end=" ")
```

### Reverse a String
```python
def reversStr(s):
    j=len(s)-1
    ans=""
    while j>=0:
        ans+=s[j]
        j-=1
    return ans
```

### Check Prime Number
```python
def isprime (n):
 if type(n)==int:
    if i<=1 :
        return False
    i=2
    while i*i<=n :
        if n%i==0 :
            return False
        i+=1
    return True
 else:
     return "not a number "
```

### Count Vowels in String
```python
def countWovwl(s):
    if type(s)==str:
        fre=0
        for i in s:
            if((i=='a'or i=="A") or (i=='e' or i=="E") or (i=='i'or i=='I') or (i=='o' or i=='O') or (i=='u'or i=='U')) :
                fre+=1
        print("wovel Numbers are ",fre)        
    else:
        print("invalid input")            
```

### Check if Given String is Palindrome
```python
def isPalindrom(s):
    j = len(s)-1
    i = 0
    while j>i:
       if s[j]!=s[i]:
           return False
       j-=1
       i+=1
    return True
```

### Reverse a Number
```python
def reverNum(n):
    if type(n)==int:
        rev=0
        p=1
        while n>0:
            parity= n%10
            rev=parity+10*rev
            n//=10
        return rev
    else:
        print("invalid input")
```

### Sum of Digits
```python
def sumofNum(num):
    if(type(num)==int):
        sum =0
        while num>0:
            parity=num%10
            sum+=parity
            num//=10
        return sum
    else:
        print("Invalid input")
```

### Return Max From List
```python
def  maxInList(list):
    if len(list)==0: 
        return -1
    max =-1999
    i=0
    for i in list:
        if i>max:
            max=i
    return max
```

### Factorial Function
```python
def fact(n):
    f=1
    while n>=1:
        f=f*n
        n-=1
    return f
```