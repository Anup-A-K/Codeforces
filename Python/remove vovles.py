z=input()
x=[]
y='aeiou'
for i in range(len(z)):
    x.append(z[i])
for i in x:
    if i not in y:
        print(i,end='')


        
