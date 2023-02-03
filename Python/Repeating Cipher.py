n=int(input())
t=input()
i=1
p=t[0]
f=1
while i<n-1:
  p=p+t[i]
  f=f+1
  i=(i+f)
print(p)
