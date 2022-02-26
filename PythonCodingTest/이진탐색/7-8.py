n, m = list(map(int, input().split()))
array = list(map(int, input().split()))

# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(array)

# 이진탐색 수행
result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    # 잘렸을 때의 떡의 양
    for x in array:
        if x > mid:
            total += x - mid

    # 떡의 양이 부족하면 더 많이 자름
    if total < m:
        end = mid - 1

    # 떡의 양이 충분하면 덜자름 (오른쪽 탐색)
    else:
        result = mid # 최대한 덜 잘랐을 때가 정답
        start = mid + 1

print(result)
