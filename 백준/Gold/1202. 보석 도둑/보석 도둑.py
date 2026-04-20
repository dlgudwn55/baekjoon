import sys
import heapq

input = sys.stdin.readline

n, k = map(int, input().split())

gems = []
for _ in range(n):
    m, v = map(int, input().split())
    gems.append((m, v))

bags = []
for _ in range(k):
    bags.append(int(input()))

gems.sort()
bags.sort()

heap = []
gem_idx = 0
ans = 0

for bag in bags:
    while gem_idx < n and gems[gem_idx][0] <= bag:
        heapq.heappush(heap, -gems[gem_idx][1])
        gem_idx += 1
    
    if heap:
        ans -= heapq.heappop(heap)

print(ans)