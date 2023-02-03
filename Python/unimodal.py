n = int(input())
l = list(map(int,input().split()))
s = 0
i = 0
for i in range(0,n-1):
    if l[i]<l[i+1]:
        s = s+1
    else:
        break
for i in range(i,n-1):
    if l[i] == l[i+1]:
        s = s+1
    else:
        break
for i in range(i,n-1):
    if l[i]>l[i+1]:
        s = s+1
    else:
        break
if s == n-1:
    print("YES")
else:
    print("NO")
