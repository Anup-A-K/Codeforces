s=input()
t=input()
a=[]
b=[]
for i in s:
    a.append(i)
for j in t:
    b.append(j)
if len(a)>len(b):
    max=len(a)
    min=len(b)
else:
    max=len(b)
    min=len(a)
ans=len(a)+len(b)
count=0
if a[-1]!=b[-1]:
    print(ans)
else:
    a.reverse()
    b.reverse()
    for y in range(min):
        if a[y]==b[y]:
            count+=2
        else:
            break
    print(ans-count)
