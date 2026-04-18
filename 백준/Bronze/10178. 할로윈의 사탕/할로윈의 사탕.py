import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    c, v = map(int, input().split())
    q = c // v
    r = c % v
    print(f"You get {q} piece(s) and your dad gets {r} piece(s).")