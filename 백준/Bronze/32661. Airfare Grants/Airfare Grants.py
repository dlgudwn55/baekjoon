import sys
input = sys.stdin.readline

p = []
n = int(input())
for _ in range(n):
    p.append(int(input()))

limit = max(p) // 2
cheapest = min(p)
print(cheapest - min(limit, cheapest))