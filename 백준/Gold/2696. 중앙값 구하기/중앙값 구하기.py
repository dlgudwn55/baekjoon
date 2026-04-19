import sys
import heapq

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    m = int(input())
    num_lst = []
    for _ in range((m-1) // 10 + 1):
        row = list(map(int, input().split()))
        num_lst.extend(row)
    
    mn_heap = []
    mx_heap = []
    result = []
    for i, num in enumerate(num_lst):
        if not mx_heap or num <= -mx_heap[0]:
            heapq.heappush(mx_heap, -num)
        else:
            heapq.heappush(mn_heap, num)

        if len(mx_heap) > len(mn_heap) + 1:
            tmp = -heapq.heappop(mx_heap)
            heapq.heappush(mn_heap, tmp)
        elif len(mx_heap) < len(mn_heap):
            tmp = -heapq.heappop(mn_heap)
            heapq.heappush(mx_heap, tmp)
        
        if i % 2 == 0:
            result.append(-mx_heap[0])
    
    print((m+1) // 2)
    for i in range(len(result)):
        print(result[i], end=" ")
        if i % 10 == 9:
            print()