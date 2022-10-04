import sys

from collections import deque

input = sys.stdin.readline

n = int(input())

d = deque(list(enumerate(map(int, input().split()))))

while len(d) > 0:
    a, b = d.popleft()

    print(a+1, end=" ")

    if b>0:
        d.rotate(-(b-1)) # rotate: 목록을 회전시킬 수 있음 (양수면 오른쪽, 음수면 왼쪽)

    else:
        d.rotate(-b)