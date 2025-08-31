def play(a, b):
    if a == 1:
        if b == 1:
            return 0
        if b == 2:
            return 2
        if b == 3:
            return 1
    elif a == 2:
        if b == 1:
            return 1
        if b == 2:
            return 0
        if b == 3:
            return 2
    else:
        if b == 1:
            return 2
        if b == 2:
            return 1
        if b == 3:
            return 0

n = int(input())
team_1 = list(map(int, input().split()))
team_2 = list(map(int, input().split()))

ans = 0
win_count = [0, 0]
for i in range(n):
    tmp = play(team_1[i], team_2[i])
    if tmp == 1:
        win_count[0] += 1
        ans = max(win_count[1], ans)
        win_count[1] = 0
    elif tmp == 2:
        win_count[1] += 1
        ans = max(win_count[0], ans)
        win_count[0] = 0
    else:
        if win_count[0] == 0:
            win_count[0] += 1
            ans = max(win_count[1], ans)
            win_count[1] = 0
        else:
            win_count[1] += 1
            ans = max(win_count[0], ans)
            win_count[0] = 0
    # print(win_count)
    ans = max(ans, win_count[0], win_count[1])

print(ans)