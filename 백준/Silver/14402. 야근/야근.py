from collections import defaultdict
import sys
input = sys.stdin.readline

data = defaultdict(list)
name_counter = defaultdict(int)
q = int(input())
for _ in range(q):
    s, p = input().strip().split()
    data[s].append(p)

# print(data)
ans = 0
for name, history in data.items():
    for action in history:
        if action == '+':
            name_counter[name] += 1
        else:
            if name_counter[name] == 0:
                ans += 1
            else:
                name_counter[name] -= 1
    ans += name_counter[name]
    
print(ans)