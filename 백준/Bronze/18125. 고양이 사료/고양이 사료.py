r, c = map(int, input().split())
rotated = []
original = []
for _ in range(c):
    rotated.append(list(input().split()))

for _ in range(r):
    original.append(list(input().split()))
    
flag = True
for i in range(r):
    for j in range(c):
        if original[i][j] != rotated[c-j-1][i]:
            flag = False
            break
    if not flag:
        break
    
if flag:
    print("""|>___/|        /}
| O < |       / }
(==0==)------/ }
| ^  _____    |
|_|_/     ||__|""")

else:
    print("""|>___/|     /}
| O O |    / }
( =0= )\"\"\"\"  \\
| ^  ____    |
|_|_/    ||__|""")
