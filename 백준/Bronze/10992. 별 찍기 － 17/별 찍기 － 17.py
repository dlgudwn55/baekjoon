n = int(input())

if n == 1:
    print('*')
    exit()

for i in range(n-1):
    print(' ', end='')
print('*')

for i in range(1, n-1):
    for j in range(n-i-1):
        print(' ', end='')
    print('*', end='')
    for j in range(i*2-1):
        print(' ', end='')
    print('*')

print('*'*(n*2-1))