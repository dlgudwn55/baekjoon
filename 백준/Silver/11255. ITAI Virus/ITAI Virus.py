from collections import defaultdict
import sys
read = sys.stdin.readline

t = int(read())
for _ in range(t):
    n, m, k = map(int, read().split())
    graph = defaultdict(list)
    for _ in range(m):
        a, b = map(int, read().split())
        graph[a].append(b)
        graph[b].append(a)
    origins = list(map(int, read().split()))
    infected = set()
    for origin in origins:
        infected.add(origin)

    for origin in origins:
        for adj in graph[origin]:
            infected.add(adj)

    print(len(infected))