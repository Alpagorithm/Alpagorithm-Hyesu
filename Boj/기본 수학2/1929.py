m, n = map(int, input().split())
list = []

for i in range(0, n+1):
    list.append(i)
list[1] = 0

for i in range(2, n+1):
    if list[i] == 0:
        continue
    j = 2
    while i*j <= n:
        list[i*j] = 0
        j = j+1

for i in range(m, n+1):
    if list[i] != 0:
        print(list[i])