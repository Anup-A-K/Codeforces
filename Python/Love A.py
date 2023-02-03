s=input()
l=len(s)
count=0
for i in range(l):
    if s[i]=='a':
        count+=1
if count>l//2:
    print(l)
else:
    print((count*2)-1)

