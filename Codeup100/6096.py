inputList = []
for i in range(0, 19):
    inputList.append(list(map(int, input().split())))

n = int(input())
nlist = []
for i in range(0, n):
    x, y = input().split()
    x = int(x)
    y = int(y)
    nlist.append([x, y])

for i in range(0, n):
    for j in range(0, 19):
        inputList[nlist[i][0] - 1][j] = abs(1 - inputList[nlist[i][0] - 1][j])
        inputList[j][nlist[i][1] - 1] = abs(1 - inputList[j][nlist[i][1] - 1])

for i in range(0, 19):
    for j in range(0, 19):
        print(inputList[i][j], end=" ")
    print()