# 회의실배정

import sys

input = sys.stdin.readline

n = int(input())
card = [0] + list(map(int, input().split()))

d = [0] * (n+1)

d[1] = card[1]

for i in range(1, n+1):
    for j in range(1, i+1):
        d[i] = max(d[i-j] + card[j], d[i])

print(d[n])
