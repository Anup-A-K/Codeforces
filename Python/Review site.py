t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    up = 0
    down = 0
    for i in l:
        if i==1:
            up+=1
        elif i==2:
            down+=1
        else:
            up+=1
            
    print(up)
