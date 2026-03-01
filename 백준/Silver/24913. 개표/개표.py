import sys
input = sys.stdin.readline

n, q = map(int, input().split())

vote_dict = {i: 0 for i in range(1, n+2)}
max_not_jeonghu = 0
sum_not_jeonghu = 0

for _ in range(q):
    arg_lst = list(map(int, input().split()))
    if arg_lst[0] == 1:
        x, p = arg_lst[1:]
        vote_dict[p] += x
        if p <= n:
            max_not_jeonghu = max(max_not_jeonghu, vote_dict[p])
            sum_not_jeonghu += x
    else:
        x, y = arg_lst[1:]
        if (vote_dict[n+1] + x > max_not_jeonghu) and \
            ((vote_dict[n+1] + x - 1)*n >= sum_not_jeonghu + y):
            print('YES')
        else:
            print('NO')