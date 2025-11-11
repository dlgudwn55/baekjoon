tn = 0
while True:
    p, s = map(int, input().split())
    if p == 0:
        break
    tn += 1
    print(f"Hole #{tn}")
    if s == 1:
        print("Hole-in-one.")
    elif s-p == -3:
        print("Double eagle.")
    elif s-p == -2:
        print("Eagle.")
    elif s-p == -1:
        print("Birdie.")
    elif s-p == 0:
        print("Par.")
    elif s-p == 1:
        print("Bogey.")
    else:
        print("Double Bogey.")
    print()