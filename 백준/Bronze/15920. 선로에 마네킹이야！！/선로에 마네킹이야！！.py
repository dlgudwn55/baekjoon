n = int(input())
s = input()

if s.count("W") < 2:
    print(0)
else:
    ans = 0
    time = 0
    lever_state = 0
    multi_track = False
    for i in range(n):
        if s[i] == "P":
            lever_state = 1 - lever_state
            if time == 1:
                multi_track = True
        else:
            time += 1
            if time == 2:
                if multi_track:
                    ans = 6
                else:
                    if lever_state == 0:
                        ans = 5
                    else:
                        ans = 1
    print(ans)