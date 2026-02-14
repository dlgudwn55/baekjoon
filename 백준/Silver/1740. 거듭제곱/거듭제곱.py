n = int(input())
bits = bin(n)[2:]
ans = 0
for i in range(len(bits)):
    ans += int(bits[i]) * 3 ** (len(bits)-i-1)
print(ans)