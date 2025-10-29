ans = 0
for _ in range(4):
    m, step = input().split()
    step = int(step)
    if m == 'Es':
        ans += 21 * step
    else:
        ans += 17 * step
        
print(ans)