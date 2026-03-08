n = int(input())
for i in range(n):
    row = [" "]*(n-i-1)+["* "]*i+["*"]
    print("".join(row))