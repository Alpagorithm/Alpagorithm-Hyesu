import heapq
import sys

input = sys.stdin.readline

heap = []
n = int(input())

for _ in range(n):
    heapq.heappush(heap, int(input()))

print(heapq)