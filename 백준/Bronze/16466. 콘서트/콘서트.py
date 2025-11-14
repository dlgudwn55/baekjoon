n = int(input())
a = list(map(int, input().split()))
a.sort()
if n == 1:
    if a[0] == 1:
        print(2)
    else:
        print(1)
else:
    if a[0] > 1:
        print(1)
    else:
        ans = 0
        for i in range(n-1):
            if a[i+1]-a[i] > 1:
                ans = (a[i]+1)
                break
        if ans != 0:
            print(ans)
        else:
            ans = a[-1]+1
            print(ans)