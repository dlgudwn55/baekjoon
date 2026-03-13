import sys

input = sys.stdin.readline

n = int(input())
for _ in range(n // 2):
    a1 = float(input())
    a2 = float(input())

    h1 = int(a1 / 22.5)
    h2 = int(a2 / 22.5)
    
    val = h1 * 16 + h2
    # print(val)
    print(chr(val), end="")