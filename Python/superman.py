z=input()
x=input()
c="aeiou"
count=0
for i in range(len(z)):
    if z[i] in c and x[i] in c:
        count+=1
    else:
        count-=1
if count>0:
    print('YES')
else:
    print('NO')

