a = int(input())
b = int(input())
c = int(input())

ans = 0
lst = [a, b, c]
lst.sort()
while not(lst[0] == lst[1] == lst[2]):
    diff = lst[2] - lst[0]
    lst[0] += diff
    lst[1] += diff
    ans += diff
    lst.sort()
print(ans)