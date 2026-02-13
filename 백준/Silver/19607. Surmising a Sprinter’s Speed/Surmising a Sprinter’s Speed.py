import sys
input = sys.stdin.readline

measurements = []
for _ in range(int(input())):
    t, x = map(int, input().split())
    measurements.append((t, x))

measurements.sort()

ans = 0
for i in range(len(measurements)-1):
    dx = abs(measurements[i+1][1] - measurements[i][1])
    dt = measurements[i+1][0] - measurements[i][0]
    speed = dx / dt
    ans = max(ans, speed)
print(ans)