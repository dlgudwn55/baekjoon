import sys
input = sys.stdin.readline

t = int(input())
for tn in range(1, t+1):
    n = int(input())
    c = list(map(int, input().split()))
    
    total_xor = 0
    for i in range(n):
        total_xor = total_xor ^ c[i]
    
    if total_xor != 0:
        print(f"Case #{tn}: NO")
        continue

    print(f"Case #{tn}: {sum(c) - min(c)}")