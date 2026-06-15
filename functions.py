# Print a Given List
def sum(list):
    for i in list:
        print(i)

# Reverse a List Using Two Pointers
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

# Reverse a String

def reversStr(s):
    j=len(s)-1
    ans=""
    while j>=0:
        ans+=s[j]
        j-=1
    return ans

# Check Prime Number
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

# Count Vowels in String
def countWovwl(s):
    if type(s)==str:
        fre=0
        for i in s:
            if((i=='a'or i=="A") or (i=='e' or i=="E") or (i=='i'or i=='I') or (i=='o' or i=='O') or (i=='u'or i=='U')) :
                fre+=1
        print("wovel Numbers are ",fre)        
    else:
        print("invalid input")

# Check if Given String is Palindrome
def isPalindrom(s):
    j = len(s)-1
    i = 0
    while j>i:
       if s[j]!=s[i]:
           return False
       j-=1
       i+=1
    return True

# Reverse a Number
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

# Sum of Digits
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
# Return Max From List
def  maxInList(list):
    if len(list)==0: 
        return -1
    max =-1999
    i=0
    for i in list:
        if i>max:
            max=i
    return max

# Factorial Function
def fact(n):
    f=1
    while n>=1:
        f=f*n
        n-=1
    return f
