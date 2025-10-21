while True:
    n = int(input())
    if n == -1:
        break
    s = []
    t = []
    for _ in range(n):
        mph, time = map(int, input().split())
        s.append(mph)
        t.append(time)
    ans = s[0]*t[0]
    for i in range(1, n):
        ans += s[i]*(t[i]-t[i-1])
    print(f"{ans} miles")