a=int(input())
for i in range(a):
    x=input()
    y=list(input().split())
    z=sorted(y)
    if z[0]!=z[1]==z[2]:
        print((y.index(z[0]))+1)
    elif z[-1]!=z[-2]==z[-3]:
        print((y.index(z[-1]))+1)

'''from collections import Counter
def unique():
    a=int(input())
    for i in range(a):
        n=int(input())
        y=list(input().split())
        C=Counter(y)
        for i in y:
            if C[i]==1:
                print(y.index(i)+1)
unique()'''
