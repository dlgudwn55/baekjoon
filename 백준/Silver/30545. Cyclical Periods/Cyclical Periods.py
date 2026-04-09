import sys
input = sys.stdin.readline

n = int(input())
data = []
for _ in range(n):
    p, s = input().split()
    p = int(p)
    data.append((p, s))

pos_dict = {}
for p, s in data:
    for i, c in enumerate(s):
        if c not in pos_dict.keys():
            pos_dict[c] = [(p, i)]
        elif len(pos_dict[c]) == 1:
            pos_dict[c].append((p, i))
        else:
            continue

# print(pos_dict)

pos_info = list(pos_dict.items())
pos_info.sort(key=lambda x: (x[1][0][0]-x[1][1][0], x[1][0][0], x[1][1][1]))

# print(pos_info)

print(pos_info[0][0])