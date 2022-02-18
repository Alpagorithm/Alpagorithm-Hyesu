import sys
input = sys.stdin.readline()

n = int(input())
list = []
for i in range(n):
    k = int(input())
    list.append(k)

list.sort()
for i in list:
    print(i)