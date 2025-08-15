import sys
input = sys.stdin.readline

ans = 0

n = int(input())
strings = []
for _ in range(n):
    strings.append(input().strip())

tmp = strings[0]
for s in strings[1:]:
    if len(s) < len(tmp):
        tmp = s

i = 0
j = 0
while i < len(tmp) and j < len(tmp):
    flag = True
    # print(i, j)
    for s in strings:
        if tmp[i:j+1] not in s:
            flag = False
            break
    if flag:
        ans = max(ans, j-i+1)
        j += 1
        
    else:
        i += 1
        if i > j:
            j += 1

print(ans)