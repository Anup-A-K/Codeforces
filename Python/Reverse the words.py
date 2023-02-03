'''x=list(map(str,input().split()))
for i in x:
    print(i[::-1],end=" ")'''

'''x=list(input())
c=len(x)
y=[]
for i in range(-1,-c-1,-1):
    y.append(x[i])
print(y)
for j in range(len(y)):
    if y[j]!=' ':
        print(y[j],end='')
    else:
        print(' ',y[j],end='')'''
s=list(map(str,input().split()))
for i in range(len(s)):
    print
for i in reversed(s):
    print(i,end='')
