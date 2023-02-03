n=int(input())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
for i in range(len(x)):
    if y[i]-x[i]!=10:
        print(x[i],y[i],end=" ")
