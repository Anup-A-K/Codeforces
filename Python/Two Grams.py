x=int(input())
s=str(input())
a=[]
for i in range(x-1):
    z=s[i:i+2]
    a.append(z)
b=0
c=0
for i in range(len(a)):
    if a.count(a[i])>b:
        b=a.count(a[i])
        c=i
print(a[c])



'''n=int(input())
x=input()
a=[]
for i in range(n-1):
    t=x[i]+x[i+1]
    a.append(t)
m=0
b=' '
for i in a:
    if a.count(i)>m:
        m=a.count(i)
        b=i
print(b)'''




'''n=int(input())
s=input()
D={ }
max_val=0
ans= None
for i in range (1, len(s)):
    t=s[i-1]+s[i];
    if t in D:
        D[t]==D[t]+1
    else:
        D[t]=1
    if D[t] > max_val:
        max_value = D[t]
        ans = t
print(ans)'''
