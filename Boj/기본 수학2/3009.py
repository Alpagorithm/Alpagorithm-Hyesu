xList = []
yList = []
for i in range(3):
    x, y = map(int, input().split())
    xList.append(x)
    yList.append(y)


if xList.count(xList[0]) == 1:
    print(xList[0], end=" ")
elif xList.count(xList[1]) == 1:
    print(xList[1], end = " ")
elif xList.count(xList[2]) == 1:
    print(xList[2], end = " ")


if yList.count(yList[0]) == 1:
    print(yList[0], end=" ")
elif yList.count(yList[1]) == 1:
    print(yList[1], end = " ")
elif yList.count(yList[2]) == 1:
    print(yList[2], end = " ")