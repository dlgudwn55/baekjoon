from collections import defaultdict
import sys
import math

input = sys.stdin.readline

n, m, q = map(int, input().split())

stock_data = defaultdict(int)  # 보유 주식
company_data = defaultdict(int)  # 회사별 주가
group_data = defaultdict(list)  # 그룹별 회사
for _ in range(n):
    g, h, p = input().strip().split()
    g = int(g)
    p = int(p)
    group_data[g].append(h)
    company_data[h] = p
    stock_data[h] = 0

for _ in range(q):
    instruction = input().strip()
    arg_lst = instruction.split()
    cmd = int(arg_lst[0])
    
    if cmd in [1, 2]:
        a, b = arg_lst[1:]
        b = int(b)
        if cmd == 1:
            cost = company_data[a] * b
            if cost > m:
                continue
            else:
                m -= cost
                stock_data[a] += b

        else:
            sell_amount = min(stock_data[a], b)
            stock_data[a] -= sell_amount
            m += sell_amount * company_data[a]

    elif cmd == 3:
        a, c = arg_lst[1:]
        company_data[a] += int(c)

    elif cmd == 4:
        d, c = map(int, arg_lst[1:])
        for company in group_data[d]:
            company_data[company] += c

    elif cmd == 5:
        d, e = map(int, arg_lst[1:])
        for company in group_data[d]:
            company_data[company] = (company_data[company] * (100 + e)) // 100
            company_data[company] = (company_data[company] // 10) * 10

    elif cmd == 6:
        print(m)

    else:
        evaluation = 0
        for stock, amount in stock_data.items():
            if amount > 0:
                evaluation += company_data[stock] * amount
        print(m + evaluation)