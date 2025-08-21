import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    tiles = list(input().split())
    flag = False
    for i in range(n-2):
        n1 = int(tiles[i][:len(tiles[i])-1])
        c1 = tiles[i][-1]
        for j in range(i+1, n-1):
            n2 = int(tiles[j][:len(tiles[j])-1])
            c2 = tiles[j][-1]
            for k in range(j+1, n):
                n3 = int(tiles[k][:len(tiles[k])-1])
                c3 = tiles[k][-1]
                if n1 == n2 == n3 and c1 != c2 and c2 != c3 and c3 != c1:
                    flag = True
                    break
                tmp = sorted([n1, n2, n3])
                if tmp[0] + 1 == tmp[1] and tmp[1] + 1 == tmp[2] and c1 == c2 == c3:
                    flag = True
                    break
            if flag:
                break
        if flag:
            break
    if flag:
        print("YES")
    else:
        print("NO")
