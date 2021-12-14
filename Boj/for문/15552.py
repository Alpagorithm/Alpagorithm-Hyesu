import sys
input = sys.stdin.readline

n = int(input())

for i in range(0, n):
    a, b = map(int, input().split())
    print(a+b)