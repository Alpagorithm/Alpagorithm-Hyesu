while True:
    data = list(map(int, input().split()))
    if data[0] == 0 and data[1] == 0 and data[2] == 0:
        break
    maxNum = max(data)
    data = set(data) - set([maxNum])
    sum = 0
    for i in data:
        sum += i*i
    if sum == maxNum * maxNum:
        print("right")
    else:
        print("wrong")