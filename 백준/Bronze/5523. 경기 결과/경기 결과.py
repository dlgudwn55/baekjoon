import sys
input = sys.stdin.readline

n = int(input())
wa, wb = 0 , 0
for _ in range(n):
    a, b = map(int, input().split())
    if a > b:
        wa += 1
    elif a < b:
        wb += 1

print(wa, wb)