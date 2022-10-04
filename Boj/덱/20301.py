import sys
from collections import deque

input = sys.stdin.readline

n, k, m = map(int, input().split())

d = deque()

for i in range(n):
    d.append(i + 1)

goRight = False
idx = 0
people = 0

while len(d) > 0:
    if goRight:
        idx += 1

        if idx % k == 0:
            print(d.pop())
            people += 1
            if people % m == 0:
                goRight = False
                people = 0
        else:
            d.appendleft(d.pop())


    else:
        idx -= 1

        if idx % k == 0:
            people += 1
            print(d.popleft())
            if people % m == 0:
                goRight = True
                people = 0

        else:
            d.append(d.popleft())
