import sys
input = sys.stdin.readline

n, k = map(int, input().split())
vote_info = {}
for i in range(1, n+1):
    a, b = map(int, input().split())
    vote_info[i] = ((a, b))
vote_info = list(vote_info.items())

vote_info.sort(key=lambda x: -x[1][0])
vote_info = vote_info[:k]
vote_info.sort(key=lambda x: -x[1][1])
print(vote_info[0][0])