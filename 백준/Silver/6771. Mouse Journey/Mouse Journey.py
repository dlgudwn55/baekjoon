import sys
input = sys.stdin.readline

r, c = map(int, input().split())
k = int(input())

cat_cages = set()
for _ in range(k):
    x, y = map(int, input().split())
    cat_cages.add((x-1, y-1))

dp = [[0] * c for _ in range(r)]

for i in range(r):
    if (i, 0) in cat_cages:
        break
    dp[i][0] = 1

for i in range(c):
    if (0, i) in cat_cages:
        break
    dp[0][i] = 1

for i in range(1, r):
    for j in range(1, c):
        if (i, j) in cat_cages:
            dp[i][j] = 0
            continue
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

print(dp[-1][-1])