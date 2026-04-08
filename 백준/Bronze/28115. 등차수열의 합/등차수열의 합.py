n = int(input())
a = list(map(int, input().split()))

if n == 1:
    print("YES")
    print(a[0])
    print(0)
    exit()

diff = a[1] - a[0]
for i in range(2, n):
    if a[i] - a[i-1] != diff:
        print("NO")
        exit()

print("YES")
print(*(a))
print(*([0] * n ))