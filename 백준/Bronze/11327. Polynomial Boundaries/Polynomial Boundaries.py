import sys
input = sys.stdin.readline

def calculate_polynomial(coefficients, x):
    res = 0
    for i in range(len(coefficients)):
        res += coefficients[i] * (x ** i)
    # print("f(x)=", res)
    return res

while True:
    n, *coefficients = list(map(int, input().split()))
    if n == 0:
        break
    x, y = map(int, input().split())
    polynomial_value = calculate_polynomial(coefficients, x)
    if polynomial_value == y:
        print("On")
    elif polynomial_value > y:
        print("Inside")
    else:
        print("Outside")