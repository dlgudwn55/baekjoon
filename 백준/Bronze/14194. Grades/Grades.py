for _ in range(int(input())):
    n = int(input())
    scores = list(map(int, input().split()))
    scores.sort()
    a = (scores[0] + scores[-1]) / 2
    b = sum(scores) / n
    if abs(a-b) < 1:
        print("Yes")
    else:
        print("No")