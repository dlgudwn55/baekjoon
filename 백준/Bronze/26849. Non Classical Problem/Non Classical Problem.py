n = int(input())
lst = []
for _ in range(n):
    a, b = map(int, input().split())
    lst.append(a/b)

print(min(lst), max(lst), sum(lst))