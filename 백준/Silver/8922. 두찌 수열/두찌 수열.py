import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    arr = tuple(map(int, input().split()))
    history = set()
    history.add(arr)
    while True:
        next = []
        for i in range(n-1):
            next.append(abs(arr[i]-arr[i+1]))
        next.append(abs(arr[-1]-arr[0]))
        if next.count(0) == n:
            print("ZERO")
            break
        if tuple(next) in history:
            print("LOOP")
            break
        arr = tuple(next[:])
        history.add(arr)