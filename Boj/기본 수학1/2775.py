t = int(input())
array = [[0 for col in range(15)] for row in range(15)]

for i in range(0, 15):
    array[0][i] = 1

for i in range(0, 15):
    array[i][0] = i


for i in range(0, 15):
    for j in range(1, 15):
        array[i][j] = array[i-1][j] + array[i][j-1]


for i in range(t):
    k = int(input())
    n = int(input())
    print(array[n][k])