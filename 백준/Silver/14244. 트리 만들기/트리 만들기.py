from collections import defaultdict

n, m = map(int, input().split())

tree = defaultdict(list)
tree[0] = [i for i in range(1, n)]

leaf_num = n - 1
prev = 1
while True:
    if leaf_num == m:
        break
    tmp = tree[0].pop()
    tree[prev].append(tmp)
    prev = tmp
    leaf_num -= 1

for k in tree:
    for v in tree[k]:
        print(k, v)