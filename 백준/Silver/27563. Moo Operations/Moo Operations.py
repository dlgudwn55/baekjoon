import sys
input = sys.stdin.readline

def solve(s: str):
    if len(s) < 3:
        return -1
    moo = s.find("MOO")
    if moo != -1:
        return moo + len(s) - (moo + 3)
    mom = s.find("MOM")
    if mom != -1:
        return mom + len(s) - (mom + 3) + 1
    ooo = s.find("OOO")
    if ooo != -1:
        return ooo + len(s) - (ooo + 3) + 1
    oom = s.find("OOM")
    if oom != -1:
        return oom + len(s) - (oom + 3) + 2
    return -1

q = int(input())
for _ in range(q):
    s = input().strip()
    print(solve(s))