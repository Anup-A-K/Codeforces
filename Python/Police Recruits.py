n = int(input())
a = list(map(int, input().split()))
free = 0
solved = 0
for i in range(n):
    if a[i] > 0:
        free += a[i] 
    if free > 0 and a[i] == -1:
        solved += 1
        free-=1
print(a.count(-1)-solved)
