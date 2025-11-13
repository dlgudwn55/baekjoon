def check(r, c, char):
    cur = [['' for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            if i == r and j == c:
                cur[i][j] = char
            else:
                cur[i][j] = board[i][j]
    for row in cur:
        if ''.join(row) == char*3:
            return True
    
    for i in range(3):
        tmp = []
        for j in range(3):
            tmp.append(cur[j][i])
        if ''.join(tmp) == char*3:
            return True
    tmp = []
    for i in range(3):
        tmp.append(cur[i][i])
    if ''.join(tmp) == char*3:
        return True
    tmp = []
    for i in range(3):
        tmp.append(cur[i][2-i])
    if ''.join(tmp) == char*3:
        return True
    
turn = input()
board = []
for _ in range(3):
    row = input()
    board.append(row)

for i in range(3):
    for j in range(3):
        if board[i][j] == 'E':
            if check(i, j, turn):
                print(i+1, j+1)
