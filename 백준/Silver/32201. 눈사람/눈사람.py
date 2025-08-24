n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

rank_a = dict()
rank_b = dict()

for i in range(n):
    rank_a[a[i]] = i
    rank_b[b[i]] = i

ans = []
most_improved = -999999
for num in rank_b.keys():
    improved = rank_a[num] - rank_b[num]
    if improved > most_improved:
        ans = [num]
        most_improved = improved
    elif improved == most_improved:
        ans.append(num)

print(*ans)