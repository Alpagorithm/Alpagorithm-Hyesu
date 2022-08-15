from collections import deque
import sys
input = sys.stdin.readline

d = deque()

k = int(input())

for _ in range(k):
    i = int(input())
    if i == 0:
        d.pop()
    else:
        d.append(i)

print(sum(d))