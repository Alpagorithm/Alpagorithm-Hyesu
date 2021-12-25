n = int(input())
list = []
for i in range(0, 123456*2+1):
    if i == 1 or i == 0:
        list.append(0)
    else:
        list.append(i)

for i in range(2, len(list)):
    if list[i] == 0:
        continue
    else:
        j = 2
        while i*j < len(list):
            list[i*j] = 0
            j = j+1

while True:
    res = 0
    for i in range(n+1, 2 * n + 1):
        if list[i] != 0:
            res = res+1
    print(res)
    n = int(input())
    if n == 0:
        break

