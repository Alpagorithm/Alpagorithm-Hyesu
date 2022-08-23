import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

d = deque()

for i in range(n):
    d.append(i+1)

print("<", end="")

idx = 0
while len(d) > 0:
    idx += 1

    if idx == k:
        idx = 0
        if len(d) == 1:
            print(d.popleft(), end=">")
        else:
            print(d.popleft(), end=", ")
    else:
        d.append(d.popleft())

