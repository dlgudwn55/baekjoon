n = int(input())
for _ in range(n):
    a, b = input().split('-')
    front = 0
    for i in range(3):
        front += (ord(a[i])-65)*26**(2-i)
    back = int(b)
    if abs(front-back) <= 100:
        print('nice')
    else:
        print('not nice')