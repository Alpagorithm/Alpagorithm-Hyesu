import sys
input = sys.stdin.readline
n = int(input())
count_array = [0] * 10001

for _ in range(n):
    count_array[int(input())] += 1

for i in range(len(count_array)):
    for _ in range(count_array[i]):
       print(i)
