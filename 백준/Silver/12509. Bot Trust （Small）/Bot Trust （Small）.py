import sys
input = sys.stdin.readline

t = int(input())
for tn in range(1, t+1):
    line = input().strip().split()
    n = int(line[0])

    r = []
    p = []
    for i in range(1, len(line), 2):
        r.append(line[i])
        p.append(int(line[i+1]))

    blue = 1
    orange = 1
    time = 0
    press_count = 0

    while press_count < n:
        idx_blue = -1
        idx_orange = -1
        press_count += 1

        for i in range(press_count-1, n):
            if r[i].upper() == 'B':
                idx_blue = i
                break
        for i in range(press_count-1, n):
            if r[i].upper() == 'O':
                idx_orange = i
                break
        
        if idx_orange == -1:
            button = p[idx_blue]
            time += abs(blue - button) + 1
            blue = button
        
        elif idx_blue == -1:
            button = p[idx_orange]
            time += abs(orange - button) + 1
            orange = button

        else:
            blue_button = p[idx_blue]
            orange_button = p[idx_orange]
            if idx_blue < idx_orange:
                if abs(blue - blue_button) < abs(orange - orange_button):
                    if orange < orange_button:
                        orange = orange + abs(blue - blue_button) + 1
                    else:
                        orange = orange - abs(blue - blue_button) - 1
                else:
                    orange = orange_button
                time += abs(blue - blue_button) + 1
                blue = blue_button

            else:
                if abs(blue - blue_button) > abs(orange - orange_button):
                    if blue < blue_button:
                        blue = blue + abs(orange - orange_button) + 1
                    else:
                        blue = blue - abs(orange - orange_button) - 1
                else:
                    blue = blue_button
                time += abs(orange - orange_button) + 1
                orange = orange_button
                
    print(f"Case #{tn}: {time}")