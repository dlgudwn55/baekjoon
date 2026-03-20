n = int(input())
c = list(map(int, input().split()))

c.sort()

# for i in range(1, n+1):
#     print(i, end=' ')
# print()

# print(*c)

ans = 999999.
for i in range(n):
    balloon = i+1
    gas = c[i]
    if balloon < gas:
        print("impossible")
        exit()
    ans = min(ans, gas/balloon)
print(ans)