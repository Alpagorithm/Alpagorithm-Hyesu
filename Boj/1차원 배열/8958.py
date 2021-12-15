n = int(input())

for i in range(0, n):
    ans = 0 # 총점
    tmp = 0
    data = input()
    data = list(data)


    for j in range(len(data)):
        if data[j] == 'O':
            tmp = tmp+1
            ans = ans + tmp
        else:
            tmp = 0

    print(ans)