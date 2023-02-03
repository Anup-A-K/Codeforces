n=int(input())
l=list(map(int,input().split()))
s=sum(l)
if s != 0:
    print("YES")
    print(1)
    print(1,n)
    exit()
for i in range(n):
    s = s - l[i]
    if s != 0:
        print("YES")
        print(2)
        print(1,i+1)
        print(i+2,n)
        break
else:
    print ("NO")
