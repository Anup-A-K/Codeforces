n=int(input())
for i in range(0,n):
    a,b,c=map(int,input().split())
    x=max(a,b,c)
    if(a==b and b==c):
        print(1,1,1)
        continue
    elif((x==a and x==b)):
        print(1,1,x-c+1)
    elif(x==b and x==c):
        print(x-a+1,1,1)
    elif(x==c and x==a):
        print(1,x-b+1,1)
    else:
        if(x-a==0):
            print(0,x-b+1,x-c+1)
        if(x-b==0):
            print(x-a+1,0,x-c+1)
        if(x-c==0):
            print(x-a+1,x-b+1,0)
            
    
