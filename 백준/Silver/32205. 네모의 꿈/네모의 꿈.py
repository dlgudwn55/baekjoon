from collections import defaultdict
import sys

input = sys.stdin.readline

n = int(input())
edge_counter = defaultdict(int)
for _ in range(n):
    a, b, c = map(int, input().split())
    edge_counter[a]+=1
    edge_counter[b]+=1
    edge_counter[c]+=1

ans = 0
for v in edge_counter.values():
    if v > 1:
        ans = 1
print(ans)