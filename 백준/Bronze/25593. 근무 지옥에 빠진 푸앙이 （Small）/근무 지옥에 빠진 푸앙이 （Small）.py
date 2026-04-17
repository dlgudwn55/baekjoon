from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
data = []
for _ in range(n*4):
    row = list(input().strip().split())
    data.append(row)

time_dict = defaultdict(int)

for i in range(len(data)):
    for j in range(7):
        name = data[i][j]
        if name == '-':
            continue
        if i % 4 == 0:
            time_dict[name] += 4
        elif i % 4 == 1:
            time_dict[name] += 6
        elif i % 4 == 2:
            time_dict[name] += 4
        else:
            time_dict[name] += 10

if not list(time_dict.keys()):
    print("Yes")
    exit()
    
mx = max(list(time_dict.values()))
mn = min(list(time_dict.values()))

if mx - mn <= 12:
    print("Yes")
else:
    print("No")