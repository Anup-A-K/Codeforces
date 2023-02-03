#1
'''z=[]
for i in range(int(input())):
    x=str(input())
    c1=0
    c2=0
    for i in x:
        if i=='4':
            c1+=1
        if i=='7':
            c2+=1
        if c1==0 or c2==0: 
            reslut='no'
        if c1>0 and c2>0:
             if c1%2==0 and c2%2==0:
             result='yes'
        else:
            result='no'
    z.append(result)
print(*z, sep="\n")'''


'''for i in range(int(input())):
    x=input()
    a=0
    b=0
    for i in range(len(x)):
        if x[i]=='4':
            a+=1
        if x[i]=='7':
            b+=1
        if b%2==0 and a%2==0 and a>0 and b>0:
            print('yes')
        else:
            print('no')'''

#2
'''n,m=map(int,input().split())
for i in range(n):
    x=list(map(int,input().split()))
    y=sorted(x)
    z=len(y)
    b=0
    count=0
    for i in range(z):
         a=x[i]+x[z-i-1]
         if a/2>m:
            b+=1
         if b==z/2:
            count+=1
    print(count)'''

#3
x=list(map(int,input().split()))
count=0
a=[]
for i in range(len(x)-1):
    if x[i]<x[i+1]:
        count+=1
    a.append(count)
    if x[i]>x[i+1]:
        count=0
    a.append(count) 
print(max(a)+1)
































































    
    


            

            
