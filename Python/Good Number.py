n,k=map(int,input().split())
count=0
x=''
for i in range(k+1):
    x+=str(i)
for i in range(n):
    c=0
    a=input()
    for i in x:
        if i in a:
            c+=1
    if c==k+1:
        count+=1
print(count)
