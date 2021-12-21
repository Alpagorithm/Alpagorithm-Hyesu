def isPrime(k):
    if k == 1:
        return False
    for i in range(2, k):
        if k % i == 0:
            return False
    return True


m = int(input())
n = int(input())
data = []

for i in range(m, n + 1):
    if isPrime(i):
        data.append(i)

if len(data) == 0:
    print(-1)
    exit(0)

sum = 0
for i in range(len(data)):
    sum = sum + data[i]
print(sum)
print(data[0])