from collections import deque
import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break
    m = 0
    flag = False
    for i in range(1, 1000):
        q = deque([i for i in range(n)])
        while True:
            rm = q.popleft()
            if rm == 1 and not q:
                m = i
                flag = True
                break
            elif rm == 1 and q:
                break
            for _ in range(i-1):
                q.append(q.popleft())
        if flag:
            break
    print(m)