n= int(input())
while n:
    a, b, k = map(int, input().split())
    if k % 2 == 0:
        m = (a * (k // 2)) - (b * (k // 2))
    else:
        m= (a * ((k // 2) + 1)) - (b * (k // 2))
    n-=1
    print(m)
