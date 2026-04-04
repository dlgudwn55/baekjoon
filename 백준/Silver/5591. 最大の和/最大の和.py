import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = []
for _ in range(n):
    a.append(int(input()))

curr = sum(a[:k])
ans = curr
for i in range(1, n-k+1):
    curr -= a[i-1]
    curr += a[i+k-1]
    ans = max(ans, curr)

print(ans)