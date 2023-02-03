for i in range (int(input())):
    a,b=map(int,input().split())
    x=a+b
    c=180-x
    if a==b==c==60:
        print('equilateral')
    elif a==b or a==c or b==c:
        print('isosceles')
    else:
        a!=b!=c
        print('scalene')
