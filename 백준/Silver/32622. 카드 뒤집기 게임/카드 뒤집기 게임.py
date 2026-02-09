n = int(input())
a = list(map(int, input().split()))

if n == 1:
    print(1)
    exit()

# 뒤집지 않는 경우
no_flip = 1
count = 1
for i in range(1, n):
    if a[i] == a[i-1]:
        count += 1
    else:
        no_flip = max(no_flip, count)
        count = 1
no_flip = max(no_flip, count)

# left[i]: i에서 끝나는 연속 길이
left = [0]*n
left[0] = 1
for i in range(1, n):
    if a[i] == a[i-1]:
        left[i] = left[i-1] + 1
    else:
        left[i] = 1

# right[i]: i에서 시작하는 연속 길이
right = [0]*n
right[-1] = 1
for i in range(n-2, -1, -1):
    if a[i] == a[i+1]:
        right[i] = right[i+1] + 1
    else:
        right[i] = 1
right.append(0)
a.append(1-a[-1])

flip = 0
for x in range(n):
    if 1-a[x] == a[x+1]:
        score = left[x] + right[x+1]
    else:
        score = max(left[x], right[x+1])
    flip = max(flip, score)

print(max(flip, no_flip))