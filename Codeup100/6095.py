n = int(input())
nlist = []
for i in range(0, n):
    x, y = input().split()
    x = int(x)
    y = int(y)
    nlist.append([x, y])

d = []

for i in range(0, 19):
    d.append([])
    for j in range(0, 19):
        d[i].append(int(0))

for i in range(0, n):
    d[nlist[i][0]-1][nlist[i][1]-1] = 1

for i in range(0, 19):
    for j in range(0, 19):
        print(d[i][j], end=" ")
    print()
