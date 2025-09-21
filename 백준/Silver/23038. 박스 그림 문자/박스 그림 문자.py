import sys
read = sys.stdin.readline

n, m = map(int, read().split())
shape = []
for _ in range(3*n):
    row = list(read().strip())
    shape.append(row)

for i in range(n):
    for j in range(m):
        if (i+j) % 2:
            if i-1>=0 and shape[3*i-1][3*j+1] == "#":
                shape[3*i][3*j+1] = "#"
                shape[3*i+1][3*j+1] = "#"
            if j-1>=0 and shape[3*i+1][3*j-1] == "#":
                shape[3*i+1][3*j] = "#"
                shape[3*i+1][3*j+1] = "#"
            if i+1<n and shape[3*(i+1)][3*j+1] == "#":
                shape[3*i+2][3*j+1] = "#"
                shape[3*i+1][3*j+1] = "#"
            if j+1<m and shape[3*i+1][3*(j+1)] == "#":
                shape[3*i+1][3*j+2] = "#"
                shape[3*i+1][3*j+1] = "#"

for row in shape:
    print(''.join(row))