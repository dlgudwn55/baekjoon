import sys
input = sys.stdin.readline

def solve(idx, curr_money):
    global M, ans
    if idx == M:
        flag = True
        for s, t, c in cows:
            for i in range(s, t+1):
                if temperatures[i] < c:
                    flag = False
                    break
            if not flag:
                break
        if flag:
            ans = min(ans, curr_money)
        return
    
    conditioner = conditioners[idx]
    for i in range(conditioner[0], conditioner[1]+1):
        temperatures[i] += conditioner[2]
    solve(idx+1, curr_money+conditioner[3])
    for i in range(conditioner[0], conditioner[1]+1):
        temperatures[i] -= conditioner[2]
    solve(idx+1, curr_money)


ans = 99999
N, M = map(int, input().split())
temperatures = [0]*101
cows = []
conditioners = []
for _ in range(N):
    s, t, c = map(int, input().split())
    cows.append((s, t, c))
for _ in range(M):
    a, b, p, m = map(int, input().split())
    conditioners.append((a, b, p, m))
solve(0, 0)
print(ans)