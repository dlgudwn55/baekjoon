import sys
input = sys.stdin.readline

n, m = map(int, input().split())
table = []
for _ in range(n):
    row = list(map(int, input().split()))
    table.append(row)
    
q = int(input())
for _ in range(q):
    row = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        flag = True
        for j in range(m):
            if row[j] == -1:
                continue
            if row[j] != table[i][j]:
                flag = False
                break
        if flag:
            ans += 1
    print(ans)