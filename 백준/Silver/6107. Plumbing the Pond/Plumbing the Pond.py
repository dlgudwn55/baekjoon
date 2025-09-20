def is_flat(x, y):
    for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < r and 0 <= ny < c:
            if pond[nx][ny] == pond[x][y]:
                return True
    return False

r, c = map(int, input().split())
pond = []
for _ in range(r):
    row = list(map(int, input().split()))
    pond.append(row)

ans = 0
for i in range(r):
    for j in range(c):
        depth = pond[i][j]
        if is_flat(i, j):
            ans = max(ans, depth)

print(ans)