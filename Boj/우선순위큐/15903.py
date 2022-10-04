import heapq
import sys

input = sys.stdin.readline

heap = []

n, m = map(int, input().split())
cardNumbers = list(map(int, input().split()))

for card in cardNumbers:
    heapq.heappush(heap, card)

for i in range(m):
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)

    heapq.heappush(heap, a + b)
    heapq.heappush(heap, a+b)

print(sum(heap))