'''def abc():
    return
def xyz(g):
    print(g+10)
v=abc()
xyz(v)'''


'''def abc(count):
    print('hello',count)
    count=count+1
    if count<10:
        abc(count)
abc(0)'''


'''def abc(n):
    if n ==0:
       return 1
    else:
         return n*abc(n-1)
ans=abc(5)
print(ans)'''

'''def abc(a,b):
    c=a*b
    print(c)
abc(int(input()),int(input()))'''

#sum of first n natural numbers using recursion.
'''def abc(n):
    if n > 0:
        return n+abc(n-1)
    else:
        return 0
ans=abc(5)
print(ans)'''


# FACTORIAL
'''def fact(a):
    if a>0:
        return a*fact(a-1)
    else:
        return 1
ans=fact(int(input()))
print(ans)'''

#MULTIPLYING TOW NUMBERS
'''def abc(a,b):
    if b>0:
        return a + abc(a,b-1)
    else:
        return 0
ans=abc(5,3)
print(ans)'''

'''def abc(x):
    a=0
    b=-1
    if len(x)<=0:
        return True
    if x[a]==x[b]:
        a=a+1
        b=b--1
        return abc(x[a:b])
    else:
        return False
x='malayalam'
ans=abc(x)
print(ans)'''

#1088A
'''x=int(input())
if x<=1:
    print('-1')
else:
    print(x,x)'''


'''n=int(input())
for i in range(n):
    x,y=map(int,input().split())
    for i in range(1,y):
        if y%i!=0 and i<=y and i%x==0 and x!=i and i>>x and i<<y:
            print(x,i)
            break'''


#978B
'''x=int(input())
z=input()
count=0
for i in range(x-2):
    if z[i]==z[i+1]==z[i+2]=='x':
        count=count+1
print(count)'''

'''def sortd(s):
    a=0
    b=a+1
    m=0
    if s[a]>s[b]:
        m=s[a]
        return m
    return sortd(s[a:b])
s=list(map(int,input().split()))
ans=sortd(s)
print(ans)'''

'''def maximum(L):
    if len(L) == 1:
        return L[0]
    else:
        return max(L[0],maximum(L[1:]))
L=list(map(int,input().split()))
s=maximum(L)
print(s)'''

'''def sum(L):
    if len(L)==1:
        return L[0]
    else:
        return (L[0]+sum(L[1:]))

L=list(map(int,input().split()))
s=sum(L)
print(s)'''

'''def mul(n):
    if n!=0:
        return n * mul(n-1)
    elif n==0:
        return 1
    
s=mul(5)
print(s)'''

'''def abc(s):
    a=0
    b=-1
    if len(s)<=1:
        return True
    elif s[a]==s[b]:
        a=a+1
        b=b--1
        return abc(s[a:b])
    else:
        return False

s=input()
x=abc(s)
print(x)'''


'''def bsort(a):
    n=len(a)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
            
a=list(map(int,input().split()))
bsort(a)
for i in range(len(a)):
    print(a[i],end=' ')'''

'''def fibo(n):
    if n<=1:
        return 1
    else:
        return n + fibo(n-1)
n=int(input())
ans=fibo(n)
print(ans)
for i in range(n+1):
    print(fibo(i))'''


'''t=list(map(int,input().split()))
def sort(t):
    for i in range(len(t)-1):
        if t[i]>t[i+1]:
            t[i],t[i+1]=t[i+1],t[i]
            return sort(t)
    return t
print(sort(t))'''

'''def mul(a):
    if len(a)<=1:
        return a[0]
    else:
        return a[0]* mul(a[1:])

a=list(map(int,input().split()))
ans=mul(a)
print(ans)'''

'''def mul(a,b):
    if b==len(a)-1:
        return a[b]
    if b<len(a):
        return a[b]* mul(a,b+1)

a=list(map(int,input().split()))
b=0
ans=mul(a,b)
print(ans)'''


'''def palin(n):
    a=0
    b=-1
    if len(n)<=1:
        return True
    elif n[a]==n[b]:
        a=a+1
        b=b--1
        return palin(n[a:b])
    else:
        return False
n=str(input())
ans=palin(n)
print(ans)'''




















































