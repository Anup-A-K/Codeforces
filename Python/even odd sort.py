x=list(map(int,input().split()))
z=[]
y=[]
for i in range(len(x)):
    if x[i]%2==0:
        z.append(x[i])
for i in range(len(x)):
    if x[i]%2!=0:
        y.append(x[i])
a=[]
for i in range(len(z)):
    a.append(z[i])
for i in range(len(y)):
    a.append(y[i])
for i in range(len(a)):
    print(a[i],end=' ')
