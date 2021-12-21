n = int(input())
data = list(map(int, input().split()))
result = 0

for i in range(len(data)):
    isPrime = True
    if data[i] == 1:
        continue
    for j in range(2, data[i]):
        if data[i] % j == 0:
            isPrime = False
            break
    if isPrime:
        result = result + 1

print(result)