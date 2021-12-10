n = int(input())
result = []

list = list(map(int, input().split()))

for i in range(0, 23):
    result.append(0)

for i in range(0, n):
    result[list[i]-1] = result[list[i]-1] + 1

for i in range(0, 23):
    print(result[i], end=" ")