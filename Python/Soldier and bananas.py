k, n, w = list(map(int, input().split()))
total_cost = 0
for i in range(1,w+1):
    total_cost +=i*k
if total_cost<=n:
    print(0)
else:
    print(total_cost-n)
