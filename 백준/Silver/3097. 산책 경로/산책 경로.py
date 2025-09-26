from math import sqrt

n = int(input())
segments = []
for _ in range(n):
    x, y = map(int, input().split())
    segments.append((x, y))
    
cx, cy = 0, 0
for x, y in segments:
    cx += x
    cy += y
    
print(cx, cy)
    
ans = 99999999.
ax, ay = 0, 0
for i in range(n):
    new_segments = segments[:i] + segments[i+1:]
    cx, cy = 0, 0
    for x, y in new_segments:
        cx += x
        cy += y
    
    if sqrt(cx**2 + cy**2) < ans:
        ans = sqrt(cx**2 + cy**2)
    # ans = min(ans, sqrt(cx**2 + cy**2))

print("%.2f" %ans)