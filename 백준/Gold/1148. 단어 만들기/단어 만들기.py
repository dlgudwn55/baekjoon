from collections import Counter
import sys
input = sys.stdin.readline

ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# 단어 입력
words = []
while True:
    word = input().strip()
    if word == "-":
        break
    words.append(word)

# 퍼즐판 입력
queries = []
while True:
    query = input().strip()
    if query == "#":
        break
    queries.append(query)

# ======
for query in queries:
    mn = 200001
    mx = 0
    center_alpha_counter = {alpha: 0 for alpha in ALPHA}

    query_alpha_counter = Counter(query)
    for word in words:
        word_alpha_counter = Counter(word)
        no_ans = False
        for char in word:
            if query_alpha_counter[char] < word_alpha_counter[char]: # 어떤 알파벳의 개수가 모자라면 다음 단어로 패스
                no_ans = True
                break

        if no_ans == False:
            for alpha in ALPHA:
                if word_alpha_counter[alpha] > 0:
                    center_alpha_counter[alpha] += 1
            
    for alpha in ALPHA:
        if query_alpha_counter[alpha] > 0:
            mn = min(center_alpha_counter[alpha], mn)
            mx = max(center_alpha_counter[alpha], mx)

    mn_center_alphas = []
    for alpha in ALPHA:
        if center_alpha_counter[alpha] == mn and query_alpha_counter[alpha] > 0:
            mn_center_alphas.append(alpha)

    mx_center_alphas = []
    for alpha in ALPHA:
        if center_alpha_counter[alpha] == mx and query_alpha_counter[alpha] > 0:
            mx_center_alphas.append(alpha)
    
    print(''.join(mn_center_alphas), mn, ''.join(mx_center_alphas), mx)