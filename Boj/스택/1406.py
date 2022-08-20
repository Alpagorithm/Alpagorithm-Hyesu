import sys
from collections import deque

input = sys.stdin.readline
s = deque()

s = deque(list(input()))
s.remove("\n")
r = deque()
m = int(input())


for _ in range(m):
    i = list(input().split())
    if i[0] == "L":
        if len(s) > 0:
          r.append(s.pop())
    elif i[0] == "D":
        if len(r) > 0:
            s.append(r.pop())
    elif i[0] == "B":
        if len(s) > 0:
            s.pop()
    elif i[0] == "P":
        s.append(i[1])

r.reverse()
print(''.join(s), end="")
print(''.join(r))
