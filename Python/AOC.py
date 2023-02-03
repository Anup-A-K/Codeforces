#1
'''z=[]
a=[]
count=0
for i in range(2000):
    x=int(input())
    z.append(x)
for i in range(len(z)-2):
    b=z[i]+z[i+1]+z[i+2]
    a.append(b)
for i in range(len(a)-1):
    if a[i]<a[i+1]:
        count+=1
print(count)'''

#2
'''a=0
f=0
d=0
for i in range(1000):
    x=list(input().split())
    if x[0]=='down':
        a=a+int(x[1])
    if x[0]=='up':
        a=a-int(x[1])
    if x[0]=='forward':
         f=f+int(x[1])
         dd=a*int(x[1])
         d=d+dd
print(f*d)'''



#3
'''a=0
aa=0
b=0
bb=0
c=0
cc=0
d=0
dd=0
e=0
ee=0
f=0
ff=0
g=0
gg=0
h=0
hh=0
i=0
ii=0
j=0
jj=0
k=0
kk=0
l=0
ll=0
ga=[]
ep=[]
for i in range(1000):
    x=list(input().split())
    for i in range(len(x)):
        if x[0][0]=='1':
            a+=1
        if x[0][0]=='0':
            aa+=1

            
        if x[0][1]=='1':
            b+=1
        if x[0][1]=='0':
            bb+=1

            
        if x[0][2]=='1':
            c+=1
        if x[0][2]=='0':
            cc+=1

            
        if x[0][3]=='1':
            d+=1
        if x[0][3]=='0':
            dd+=1

            
        if x[0][4]=='1':
            e+=1
        if x[0][4]=='0':
            ee+=1

            
        if x[0][5]=='1':
            f+=1
        if x[0][5]=='0':
            ff+=1

            
        if x[0][6]=='1':
            g+=1
        if x[0][6]=='0':
            gg+=1


        if x[0][7]=='1':
            h+=1
        if x[0][7]=='0':
            hh+=1
            

        if x[0][8]=='1':
            i+=1
        if x[0][8]=='0':
            ii+=1


        if x[0][9]=='1':
            j+=1
        if x[0][9]=='0':
            jj+=1


        if x[0][10]=='1':
            k+=1
        if x[0][10]=='0':
            kk+=1

        if x[0][11]=='1':
            l+=1
        if x[0][11]=='0':
            ll+=1

            
if a>aa:
    ga.append(1)
    ep.append(0)
if aa>a:
     g.append(0)
     e.append(1)

     
if b>bb:
    ga.append(1)
    ep.append(0)
if bb>b:
     ga.append(0)
     ep.append(1)

if c>cc:
    ga.append(1)
    ep.append(0)
if cc>c:
     ga.append(0)
     ep.append(1)

if d>dd:
    ga.append(1)
    ep.append(0)
if dd>d:
     ga.append(0)
     ep.append(1)


if e>ee:
    ga.append(1)
    ep.append(0)
if ee>e:
     ga.append(0)
     ep.append(1)

if f>ff:
    ga.append(1)
    ep.append(0)
if ff>f:
     ga.append(0)
     ep.append(1)

     
if g>gg:
    ga.append(1)
    ep.append(0)
if gg>g:
     ga.append(0)
     ep.append(1)


if h>hh:
    ga.append(1)
    ep.append(0)
if hh>h:
     ga.append(0)
     ep.append(1)


if i>ii:
    ga.append(1)
    ep.append(0)
if ii>i:
     ga.append(0)
     ep.append(1)


if j>jj:
    ga.append(1)
    ep.append(0)
if jj>j:
     ga.append(0)
     ep.append(1)


if k>kk:
    ga.append(1)
    ep.append(0)
if kk>k:
     ga.append(0)
     ep.append(1)


if l>ll:
    ga.append(1)
    ep.append(0)
if ll>l:
     ga.append(0)
     ep.append(1)

     
print(ga,ep)'''




a=0
aa=0
b=0
bb=0
c=0
cc=0
d=0
dd=0
e=0
ee=0
f=0
ff=0
g=0
gg=0
h=0
hh=0
i=0
ii=0
j=0
jj=0
k=0
kk=0
l=0
ll=0
O=[]
CO=[]
y=[]


for i in range(12):
    x=input()
    y.append(x)
for i in range(12):
    for j in range(5):
        if y[i][j]=='1':
            
        



    































   
