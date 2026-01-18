import sys
input = sys.stdin.readline

n = int(input())
accom_lst = []
for _ in range(n):
    d, c = map(int, input().split())
    accom_lst.append((d, c))

ans = 0
for i in range(n):
    flag = True
    cur_dist, cur_cost = accom_lst[i]
    for j in range(n):
        if i == j:
            continue
        dist, cost = accom_lst[j]
        if (dist <= cur_dist and cost <= cur_cost):
            flag = False
            break
    if flag:
        ans += 1

print(ans)