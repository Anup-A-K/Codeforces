n,m=map(int,input().split())
l=[]
x=0
y=0
z=0
for i in range(n):
    a,b=map(int,input().split())
    l.append(a-b)
    x+=a
    y+=b  
l.sort()
l.reverse()
while z<n and x>m:
    x=x-l[z]
    z+=1
if y>m:
    print(-1)
else:
    print(z)

''''n,m=map(int,input().split())
x=0
diff=[]
for i in range(n):
     a,b=map(int,input().split())
     x=x+a
     diff.append(abs(b-a))
     diff.sort()
     diff.reverse()
if x<=m:
     print(-1)
i=0
z,y=0,-1
while x>m and i<len(diff):
     x-=diff[i]
     z+=1
     i+=1
if z==n:
      print(-1)
else:
      print(z)'''
