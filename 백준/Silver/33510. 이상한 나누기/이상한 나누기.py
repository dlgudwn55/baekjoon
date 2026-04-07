import math

n = int(input())
x = input()

if x == '1':
    print(0)
elif x == '1' + '0'*(n-1):
    print(0)
elif x == '1' * n:
    print(1)
else:
    bits = list(x)
    ans = 0
    while bits != ['1']:
        if bits[-1] == '0':
            bits.pop()
        else:
            ans += 1
            bits[-1] = '0'
            i = -2
            while i > -len(bits) and bits[i] == '1':
                bits[i] = '0'
                i -= 1
            bits[i] = '1'
            bits.pop()
            # print(bits)
    print(ans)