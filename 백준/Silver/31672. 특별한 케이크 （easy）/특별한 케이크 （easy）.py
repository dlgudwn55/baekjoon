from collections import defaultdict
import sys
input = sys.stdin.readline

statement_dict = defaultdict(list)

input()
n = int(input())
for i in range(1, n+1):
    m = int(input())
    s = set(map(int, input().split()))
    b = int(input())
    statement_dict[i] = [s, b]

ans = []

# i 번째 학생이 범인이라고 가정
for i in range(1, n+1):
    suspects = set(range(1, n+1))
    is_contradiction = False

    # j 번째 학생의 진술 확인
    for j in range(1, n+1):
        if is_contradiction:
            break
            
        s, b = statement_dict[j]
        if i == j:
            b = 1 - b
        
        if b == 1:
            if len(suspects.intersection(s)) == 0:
                is_contradiction = True
            else:
                suspects = suspects & s
        else:
            if len(suspects.intersection(s)) != 0:
                suspects = suspects.difference(s)
                # 용의자는 적어도 한 명 이상 남아있어야 함
                if len(suspects) == 0:
                    is_contradiction = True
    
    if not is_contradiction and i in suspects:
        ans.append(i)

# 결과 출력
if ans:
    print(*ans)
else:
    print("swi")