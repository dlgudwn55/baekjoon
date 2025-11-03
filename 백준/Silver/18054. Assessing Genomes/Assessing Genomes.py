from itertools import permutations
import sys
input = sys.stdin.readline

def get_score(seq):
    l = len(seq)
    res = l
    for i in range(l):
        if l%(i+1):
            continue
        tmp = seq[:i+1]
        if tmp*(l//(i+1)) == seq:
            res = min(res,i+1)
    return res
        
n = int(input())
viruses = []
antiviruses = []
for _ in range(n):
    viruses.append(input().strip())
for _ in range(n):
    antiviruses.append(input().strip())
    
virus_scores = []
antivirus_scores = []
for v in viruses:
    virus_scores.append(get_score(v))
for a in antiviruses:
    antivirus_scores.append(get_score(a))
    
virus_scores.sort()
antivirus_scores.sort()

ans = 0
for i in range(n):
    ans += ((virus_scores[i]-antivirus_scores[i])**2)
print(ans)
