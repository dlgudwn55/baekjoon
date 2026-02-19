n = int(input())
a = list(map(int, input().split()))

a.sort()
ans = 0
right = [a[i] for i in range(n)]
for i in range(n-2, -1, -1):
    right[i] += right[i+1]

for i in range(n-1):
    cost = a[i] * right[i+1]
    ans += cost

print(ans)