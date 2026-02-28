import sys
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split()) # a: 가로 길이, b: 세로 길이
points = set()
for _ in range(n):
    x, y = map(int, input().split())
    points.add((x, y))

ans = 0
for x, y in points:
    if (x + a, y) in points and (x, y + b) in points and (x + a, y + b) in points:
        ans += 1

print(ans)