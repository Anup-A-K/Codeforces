n=int(input())
d=[]
for i in range(n):
    A=map(int,input().split())
    d.append(A)
for i in range(0,len(d)):
    print(sum(d[i]))

