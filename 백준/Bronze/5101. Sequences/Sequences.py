while True:
    a1, d, t = map(int, input().split())
    if a1 == 0 and d == 0 and t == 0:
        break
    if (t-a1)%d:
        print("X")
    else:
        if (t-a1)//d+1>0:
            print((t-a1)//d+1)
        else:print("X")