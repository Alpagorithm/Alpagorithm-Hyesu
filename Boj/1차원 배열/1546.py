n = int(input())
data = list(map(int, input().split()))

# 최고값 찾기
m = 0
for i in data:
    if m < i:
        m = i

# 새로운 점수
for i in range(0, len(data)):
    data[i] = (data[i]/m) * 100

# 새로운 평균
sum = 0
for i in data:
    sum = sum + i

print(sum / len(data))