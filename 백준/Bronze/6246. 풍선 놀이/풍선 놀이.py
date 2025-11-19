import sys
input = sys.stdin.readline

n, q = map(int, input().split())
balloons = [False] * n
for _ in range(q):
    L, i = map(int, input().split())
    L -= 1
    for k in range(L, n, i):
        balloons[k] = True
print(balloons.count(False))