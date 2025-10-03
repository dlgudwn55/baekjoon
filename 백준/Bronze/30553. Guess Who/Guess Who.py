n, m, q = map(int, input().split())
string_lst = []
for _ in range(n):
    string_lst.append(input())
    
remains = [True for _ in range(n)]
for _ in range(q):
    a, b = input().split()
    a = int(a) - 1
    for i in range(n):
        if string_lst[i][a] != b:
            remains[i] = False

if remains.count(True) == 1:
    print("unique")
    print(remains.index(True) + 1)
else:
    print("ambiguous")
    print(remains.count(True))