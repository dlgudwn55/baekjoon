import sys
input = sys.stdin.readline

eratos = {i: True for i in range(2, 10**6+1)}
for i in range(2, 10**6+1):
    if eratos[i]:
        for j in range(i*2, 10**6+1, i):
            eratos[j] = False

primes = []
for k, v in eratos.items():
    if v:
        primes.append(k)
# print("--- eratos completed ---")

def solve(n):
    if n == 1:
        return False

    factors = set()
    idx = 0
    while n > 1:
        if n % primes[idx] != 0:
            idx += 1
        else:
            factors.add(str(primes[idx]))
            n //= primes[idx]
    
    for factor in factors:
        if factor[-1] != "3":
            return False
        
    return True


while True:
    n = int(input())
    if n == -1:
        break
    
    if solve(n):
        print(f"{n} YES")
    else:
        print(f"{n} NO")
