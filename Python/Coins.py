x=list(map(int,input().split()))
a=x[0]
b=x[1]
if b%a==0 :
  print(int(b/a))
else :
  print(int((b//a)+1))
