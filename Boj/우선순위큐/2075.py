import heapq
import sys

input = sys.stdin.readline

heap = []

n = int(input())

for i in range(n):
    # 한줄씩 입력
    list = map(int, input().split())

    for l in list:
        if n > len(heap):
            heapq.heappush(heap, l)
        else:
            if heap[0] < l:
                heapq.heappop(heap)
                heapq.heappush(heap, l)

print(heap[0])