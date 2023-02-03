'''s=input()
count=sum( 1 for s in s if s.isupper())
count1=sum(1 for s in s if s.islower())
if count>count1:
    print(s.upper())
elif count==count1:
    print(s.lower())
else:
    print(s.lower())'''

s=input()
l=len(s)
count=0
count1=0
for i in range(l):
    if s[i].isupper():
        count+=1
    else:
        count1+=1
if count>count1:
    print(s.upper())
elif count==count1:
    print(s.lower())
else:
    print(s.lower())
