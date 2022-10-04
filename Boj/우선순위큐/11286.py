import heapq
import sys

input = sys.stdin.readline

n = int(input())

heap = []

for i in range(n):
    x = int(input())

    if x == 0: # 배열에서 절댓값이 가장 작은 값을 출력하고 그 값을 제거
        if len(heap) > 0:
            print(heapq.heappop(heap)[1])
        else:
            print(0) #비어있으면 0 출력

    else:
        heapq.heappush(heap, (abs(x), x))