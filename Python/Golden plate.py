w,h,k=map(int,input().split())
y=0
for i in range(k):
  y=y+2*(w+h)-4
  w=w-4
  h=h-4
print(y)
