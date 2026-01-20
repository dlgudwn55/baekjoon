import sys
input = sys.stdin.readline

def is_square(points):
    distances = []  # 실제로는 거리의 제곱값 저장
    for i in range(4):
        for j in range(i + 1, 4):
            x1, y1 = points[i]
            x2, y2 = points[j]
            dist = (x1 - x2) ** 2 + (y1 - y2) ** 2
            distances.append(dist)
    
    distances.sort()
    
    # 정사각형 조건:
    # 1. 처음 4개의 거리(변)가 모두 같아야 함
    # 2. 마지막 2개의 거리(대각선)가 같아야 함
    if distances[0] == distances[1] == distances[2] == distances[3] and distances[4] == distances[5]:
        return 1
    return 0

t = int(input())
for _ in range(t):
    points = []
    for _ in range(4):
        a, b = map(int, input().split())
        points.append((a, b))
    
    print(is_square(points))
