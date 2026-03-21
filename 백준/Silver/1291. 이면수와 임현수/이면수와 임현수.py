# 2, 3, 4의 합으로 만들 수 있는 숫자들(5는 제외) 중 자릿수 합이 홀수
def check_imy(n):
    if n == 4 or n >= 6:
        s = sum([int(digit) for digit in str(n)])
        if s % 2 == 1:
            return True
        else:
            return False
    return False

# 2 또는 4이거나, 합성수이면서 소인수의 개수가 짝수
def check_imh(n):
    if n in [2, 4]:
        return True
    
    prime_factors = set()
    tmp = n
    while tmp > 1:
        for i in range(2, tmp+1):
            if tmp % i == 0:
                prime_factors.add(i)
                tmp //= i
                break
    # print(prime_factors)
    return len(prime_factors) > 0 and len(prime_factors) % 2 == 0

n = int(input())

is_imy = check_imy(n)
is_imh = check_imh(n)

if is_imy == True and is_imh == False:
    print(1)
elif is_imy == False and is_imh == True:
    print(2)
elif is_imy == False and is_imh == False:
    print(3)
else:
    print(4)