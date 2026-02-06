import sys
input = sys.stdin.readline

n, k = map(int, input().split())
scores = []
for _ in range(n):
    scores.append(float(input()))

scores.sort()

# 절사평균
print("{:.2f}".format(sum(scores[k:n-k]) / (n-2*k) + 1e-8))

# 보정평균
least = scores[k]
best = scores[n-k-1]
scores[:k] = [least]*k
scores[n-k:] = [best]*k
print("{:.2f}".format(sum(scores) / n + 1e-8))