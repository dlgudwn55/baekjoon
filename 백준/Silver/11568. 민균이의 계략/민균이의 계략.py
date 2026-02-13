from bisect import bisect_left
import sys
input = sys.stdin.readline

n = int(input())
seq = list(map(int, input().split()))

lis = []
for i in range(n):
    if len(lis) == 0:
        lis.append(seq[i])
    else:
        if lis[-1] < seq[i]:
            lis.append(seq[i])
        else:
            idx = bisect_left(lis, seq[i])
            lis[idx] = seq[i]

print(len(lis))