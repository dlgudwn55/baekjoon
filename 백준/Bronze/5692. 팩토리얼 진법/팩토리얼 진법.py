import sys
from math import factorial

input = sys.stdin.readline

while True:
  n = int(input())
  if n == 0:
    break
  n = str(n)
  ans = 0
  for i in range(len(n)):
    ans += int(n[i])*factorial(len(n)-i)
  print(ans)
