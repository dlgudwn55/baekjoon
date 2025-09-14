import sys
read = sys.stdin.readline

t = int(input())
for _ in range(t):
    r, c, message = input().strip().split()
    r = int(r)
    c = int(c)

    matrix = []
    for i in range(r):
        row = message[c*i:c*(i+1)]
        matrix.append(row)

    visit = [[False for _ in range(c)] for _ in range(r)]
    
    letter_count = len(message) // 5
    cur_count = 0
    row, col = 0, 0
    dr, dc = 0, 1
    ans = ""
    buffer = ""

    while cur_count < letter_count:
        buffer += matrix[row][col]
        visit[row][col] = True

        if len(buffer) == 5:
            val = int("0b" + buffer, base=0)
            if val == 0:
                ans += " "
            else:
                ans += chr(val + 64)
            buffer = ""
            cur_count += 1

        if row + dr >= r or col + dc >= c or visit[row + dr][col + dc]:
            if dr == 0 and dc == 1:
                dr, dc = 1, 0
            elif dr == 1 and dc == 0:
                dr, dc = 0, -1
            elif dr == 0 and dc == -1:
                dr, dc = -1, 0
            else:
                dr, dc = 0, 1
        
        row += dr
        col += dc

    print(ans.rstrip())