import sys

input = sys.stdin.readline

n = int(input())
time = []
ans = 0
before = 0

for _ in range(n):
    start, end = map(int, input().split())
    time.append((start, end))

time.sort(key=lambda a: (a[1], a[0]))

for t in time:
    if t[0] >= before:
        ans += 1
        before = t[1]

print(ans)