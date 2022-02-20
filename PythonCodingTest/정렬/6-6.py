# 계수정렬 소스코드

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# 모든 범위를 포함하는 리스트 선언 (모든 값은 0으로 초기화)
count = [0] * (max(array) + 1)

# 각 데이터에 해당하는 인덱스의 값 증가
for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end='')
