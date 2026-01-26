import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
    x5 = max(x1, x3)
    y5 = max(y1, y3)
    x6 = min(x2, x4)
    y6 = min(y2, y4)

    if (x5 < x6) and (y5 < y6):
        print((x2-x1)*(y2-y1)-(x6-x5)*(y6-y5))
    else:
        print((x2-x1)*(y2-y1))