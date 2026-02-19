n = int(input())
a = list(map(int, input().split()))

a.sort()
ans = 0

for i in range(n):
    cost = a[i] * sum(a[i+1:])
    ans += cost

print(ans)