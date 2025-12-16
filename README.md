# Question-for-python-
 
#password matching....

password=input("Enter password")
email=input("Enter mail")

if password=="1234"and email=="majid9911@gmail.com":
    print("Welcome")
else:
    print("Invalid password")

# find max 

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

#find sum of this 
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

# prime numebrs 

for i in range(10,100):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)



# coutn charecter 


s = 'Majid'
fre=0
for i in s:
    if i=='i': fre=fre+1
print(fre)



#Vowel or constant



s ="aeiou"
for i in s:
    if i=='e' or i=='i'or i=='a'or i=='o'or i=='u':
        print(i,"is vowel")
    else:
        print(i,'not a vowel')

#fibonaci



pre=0
curr=1
print(0,1,end=" ")

for i in range(3,10):
    res=pre+curr
    print(res,end=" ")
    pre=curr
    curr=res
    
 # bill calculation
units = int(input("enter consumed units"))
p_perUnit=int(input("Enter prince of one units"))



 #list sum 

list =[1,2,3,4,5,6]
sum=0

for i in list:
    sum+=i
print(sum)

# leap year

year = int(input("enter year "))
if (year%4 and year%100!=0) or year%400 :
    print(year," is leap year")
else:
    print("Not a leap year")
