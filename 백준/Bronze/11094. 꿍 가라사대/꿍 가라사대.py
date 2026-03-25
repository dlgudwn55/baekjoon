import sys

input = sys.stdin.readline
SIMON_SAYS = "Simon says"

n = int(input())
for _ in range(n):
    instruction = input().strip()
    if instruction[:10] == SIMON_SAYS:
        print(instruction[10:])
    