n=int(input())
for i in range(n):
    x=str(input())
    a=[]
    for i in x:
        a.append(int(i))
    print(sum(a))
