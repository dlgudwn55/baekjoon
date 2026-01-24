def generate_fibonacci(maxn):
    fibo = [0] * (maxn + 1)
    fibo[0] = 1
    fibo[1] = 1
    # fibo[2] = 1
    for i in range(2, maxn + 1):
        fibo[i] = fibo[i-1] + fibo[i-2]
    return fibo

fibo = generate_fibonacci(80)
n = int(input())
given = input().replace("long", "L")

n = len(given)
sequal_L_counts = []
count = 0
for i in range(n):
    if given[i] == 'L':
        count += 1
    else:
        sequal_L_counts.append(count)
        count = 0

sequal_L_counts.append(count)

ans = 1
for count in sequal_L_counts:
    ans *= fibo[count]
print(ans)