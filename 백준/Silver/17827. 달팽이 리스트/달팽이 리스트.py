import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())
c = list(map(int, input().split()))

nodes = {i: c[i] for i in range(n)}

edges = []
for _ in range(m):
    k = int(input())
    if k < v:
        print(nodes[k])
    else:
        print(nodes[(k-v+1) % (n-v+1) + (v-1)])
