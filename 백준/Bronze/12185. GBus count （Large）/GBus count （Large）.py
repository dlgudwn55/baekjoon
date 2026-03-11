import sys
input = sys.stdin.readline

t = int(input())
for i in range(1, t+1):
    n = int(input())
    lst = list(map(int, input().split()))

    a = lst[::2]
    b = lst[1::2]

    p = int(input())

    cities = []
    for _ in range(p):
        cities.append(int(input()))

    ans = []

    for city in cities:
        count = 0
        for j in range(n):
            if a[j] <= city <= b[j]:
                count += 1
        ans.append(count)

    print(f"Case #{i}:", *ans)

    if i < t:
        input()