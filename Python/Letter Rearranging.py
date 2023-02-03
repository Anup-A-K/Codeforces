n=int(input())
for i in range(n):
    s=input()
    x=[]
    y=[]
    for i in s:
        x.append(str(i))
        y.append(str(i))
    y.reverse()
    if x!=y:
        print(s)
    else:
        if x==sorted(x):
            print(-1)
        elif x==y:
            u=x.pop(0)
            x.append(u)
            for j in range(len(x)):
                print(x[j],end='')
            print()

            
'''for i in range(int(input())):
    l=list(input())
    l.sort()
    if l[0]==l[-1]:
        print(-1)
    else:
        print("".join(l))
    print(l[0] , l[-1])
    print(l)'''
