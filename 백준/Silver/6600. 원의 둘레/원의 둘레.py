import sys
input = sys.stdin.readline

PI =  3.141592653589793

# 가우스 소거법을 사용한 연립방정식 풀이
def solve_3x3(A, b):
    M = [A[i] + [b[i]] for i in range(3)]
    
    for i in range(3):
        # 피벗이 0이면 0이 아닌 행과 교환
        if M[i][i] == 0:
            for k in range(i+1, 3):
                if M[k][i] != 0:
                    M[i], M[k] = M[k], M[i]
                    break
        
        # 정규화
        pivot = M[i][i]
        for j in range(i, 4):
            M[i][j] /= pivot
        
        # 소거
        for k in range(i+1, 3):
            factor = M[k][i]
            for j in range(i, 4):
                M[k][j] -= factor * M[i][j]
    
    x = [0, 0, 0]
    for i in range(2, -1, -1):
        x[i] = M[i][3] - sum(M[i][j]*x[j] for j in range(i+1, 3))
    
    return x

def round_two(num):
    num *= 100
    num = int(num + 0.5)
    num /= 100
    return num

while True:
    input_line = input().strip()
    if input_line == "":
        break
    x1, y1, x2, y2, x3, y3 = map(float, input_line.split())

    A = [
        [x1, y1, 1],
        [x2, y2, 1],
        [x3, y3, 1]
    ]
    b = [-x1**2 - y1**2, -x2**2 - y2**2, -x3**2 - y3**2]

    a, b, c = solve_3x3(A, b)
    # print(a, b, c)

    r = ((a**2 + b**2) / 4 - c)**0.5
    print(round_two(2*PI*r))