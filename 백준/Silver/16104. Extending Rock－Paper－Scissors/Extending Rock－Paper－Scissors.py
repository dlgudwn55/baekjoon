n = int(input())

for i in range(1, n+1):
    tmp = [j for j in range(1, n+1) if i != j]
    # print(tmp)
    for j in range(i-1, (i-1) + (n-1)//2):
        print(i, tmp[j%(n-1)])
