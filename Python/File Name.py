x=int(input())
z=input()
count=0
for i in range(x-2):
    if z[i]==z[i+1]==z[i+2]=='x':
        count=count+1
print(count)
