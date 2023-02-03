x=int(input())
y=list(map(int,input().split()))
if len(y)==x:
    if 1 in y:
        result='HARD'
    else:
        result='EASY'
print(result)
