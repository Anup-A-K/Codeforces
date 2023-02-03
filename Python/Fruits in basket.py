x=int(input())
y=list(input().split())
c_r=0
c_g=0
c_y=0 
for i in range(len(y)):
    if y[i]=='red':
         c_r+=1
    elif y[i]=='green':
         c_g+=1
    else:
            c_y+=1
if c_r==c_y or c_g==c_r or c_g==c_y:
        result='none'
if c_r>c_y and c_r>c_g and c_r!=c_y and c_r!=c_g:
        result='apple'
if c_g>c_y and c_g>c_r and c_g!=c_y and c_g!=c_r:
        result='guava'
if c_y>c_g and c_y>c_r and c_y!=c_r and c_y!=c_g:
        result='banana'
print(result)

'''x=int(input())
y=list(input().split())
c_r=0
c_g=0
c_y=0
z=[] 
for i in range(len(y)):
    if y[i]=='red':
            c_r+=1
    elif y[i]=='green':
            c_g+=1
    else:
            c_y+=1
z.append(c_r)
z.append(c_g)
z.append(c_y)
if max(z)==c_r and c_r!=c_g and c_r!=c_y:
     print('apple')
elif max(z)==c_g and c_g!=c_r and c_g!=c_y:
       print('guava')
elif max(z)==c_y and c_y!=c_r and c_y!=c_g:
       print('banana')
else:
       print('none')'''
































    
