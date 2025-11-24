s = input()
t = input()
if len(s) > len(t):
    tmp = s
    s = t
    t = tmp
n = len(s)
ans = ""
for i in range(n, 0, -1):
    # print(i)
    if len(s) % i == 0 and len(t) % i == 0:
        # print(s[:i]*(len(s)//i), s[:i]*(len(t)//i))
        if s[:i]*(len(s)//i)==s and s[:i]*(len(t)//i)==t:
            ans = s[:i]
            # print(ans)
            # break
if ans:
    print(ans)
else:
    print("No solution")