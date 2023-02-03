#array sum
'''def summ(x):
    if len(x)==1:
        return x[0]
    else:
        return x[0]+ summ(x[1:])

x=list(map(int,input().split()))
print(summ(x))'''

#fibo
'''def fibo(x):
    if x<=1:
        return x
    else:
        return fibo(x-1)+fibo(x-2)
x=int(input())
for i in range(x+1):
    print(fibo(i))'''


#search key
'''def search(x,k):
    if len(x)==1 and x[0]!=k:
        return False
    elif x[0]==k:
        return True
    else:
        return search(x[1:],k)

x=list(map(int,input().split()))
k=int(input())
print(search(x,k))'''


#array max
'''def maxx(x,m):
    if len(x)==0:
        return m
    else:
        if m<x[0]:
            m=x[0]
            return maxx(x[1:],m)
        else:
            return maxx(x[1:],m)


x=list(map(int,input().split()))
m=x[0]
print(maxx(x,m))'''

#factorial
'''def fact(x):
    if x<=1:
        return 1
    else:
        return x*fact(x-1)
x=int(input())
print(fact(x))'''

#palindrome check
'''def pali(s):
    a=0
    b=-1
    if len(s)<=1:
        return True
    elif s[a]==s[b]:
        a=a+1
        b=b--1
        return pali(s[a:b])
    else:
        return False

s=str(input())
print(pali(s))'''

#2 numbers multiplication
'''def abc(a,b):
    if b>0:
        return a + abc(a,b-1)
    else:
        return 0
ans=abc(5,3)
print(ans)'''


#bubblesort
'''def bsort(x):
    n=len(x)
    for i in range(n-1):
        for j in range(n-1-i):
            if x[j]>x[j+1]:
                x[j],x[j+1]=x[j+1],x[j]

x=list(map(int,input().split()))
bsort(x)
for i in range(len(x)):
    print(x[i],end=' ')'''

#bubblesort using recursion
'''def bubblesort(l,n):
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            l[i], l[i+1] = l[i+1], l[i]
    if n>1:        
        return bubblesort(l,n-1)   

l = list(map(int,input().split()))
n=len(l)    
bubblesort(l,n)
print(l)'''


#euclid gcd
'''def egcd(x,y):
    if y==0:
        return x
    else:
        return egcd(y,x%y)
x,y=map(int,input().split())
print(egcd(x,y))'''


#array multiplication
'''def mul(x):
    if len(x)==1:
        return x[0]
    else:
        return x[0]* mul(x[1:])

x=list(map(int,input().split()))
print(mul(x))'''







