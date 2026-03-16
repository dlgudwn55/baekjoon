n, a = map(int, input().split())

def solve(n, a):
    k = 0
    pow_a = a
    while pow_a <= n:
        k += n // pow_a
        pow_a *= a
    return k

print(solve(n, a))