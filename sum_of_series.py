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