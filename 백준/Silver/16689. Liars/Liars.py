import sys
input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
    a, b = map(int, input().split())
    lst.append((a, b))

ans = -1
for i in range(1, n+1):
    count = 0
    for j in range(n):
        a, b = lst[j]
        if a <= i <= b:
            count += 1
    if count == i:
        ans = max(ans, count)

print(ans)