import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    dist1 = a ** 2 + (b + c) ** 2
    dist2 = (a + c) ** 2 + b ** 2
    dist3 = (a + b) ** 2 + c ** 2
    print(min(dist1, dist2, dist3))