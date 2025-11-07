from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
counter = defaultdict(int)
for _ in range(n):
    word = input().strip()
    counter[word] += 1

items = list(counter.items())
items.sort(key=lambda x: x[0], reverse=True)
items.sort(key=lambda x: x[1], reverse=True)

print(*items[0])