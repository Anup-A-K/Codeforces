n=int(input())
a,b,c,d=map(int,input().split())
thomas_sum=a+b+c+d
rank=1
for i in range(n-1):
     a,b,c,d=map(int,input().split())
     new_sum=a+b+c+d
     if (new_sum>thomas_sum):
          rank+=1
print(rank)
