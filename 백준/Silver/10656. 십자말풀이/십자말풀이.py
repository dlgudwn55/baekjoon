def check_row(r, c):
    if c + 2 >= m:
        return False
    for i in range(3):
        if grid[r][c + i] != '.':
            return False
    return True

def check_column(r, c):
    if r + 2 >= n:
        return False
    for i in range(3):
        if grid[r + i][c] != '.':
            return False
    return True

n, m = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]
ans = []

for r in range(n):
    for c in range(m):
        if grid[r][c] == '.' and (c == 0 or grid[r][c - 1] != '.'):
            if check_row(r, c):
                ans.append((r + 1, c + 1))
        if grid[r][c] == '.' and (r == 0 or grid[r - 1][c] != '.'):
            if check_column(r, c):
                ans.append((r + 1, c + 1))
        
ans = sorted(list(set(ans)))
print(len(ans))
for r, c in ans:
    print(r, c)