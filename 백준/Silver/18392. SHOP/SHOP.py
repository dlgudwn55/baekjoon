import sys
input = sys.stdin.readline

t = int(input())
for tn in range(1, t+1):
    m = int(input())
    line = input().strip()
    entry_lst = line.split(',')

    bill_matrix = []
    for entry in entry_lst:
        bill, number = map(int, entry.split(':'))
        bill_matrix.append([bill, number])

    bill_matrix.sort(reverse=True)

    i = 0
    ans = []
    while i < len(bill_matrix) and m > 0:
        if m >= bill_matrix[i][0]:
            count = min(bill_matrix[i][1], m // bill_matrix[i][0])
            ans.append((bill_matrix[i][0], count))
            m = m - bill_matrix[i][0] * count
        i += 1
    
    print(f"Customer{tn}:")
    if m == 0:
        for bill, number in ans:
            print(bill, number)
    else:
        print("Impossible")
    