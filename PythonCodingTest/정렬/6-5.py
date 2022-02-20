# 파이썬의 장점을 살린 퀵 정렬 소스코드

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array):
    # 리스트가 하나의 원소만 담고 있으면 종료
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]  # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    # 분할 이후 왼쪽과 오른쪽 부분에서 각각 정렬을 수행하고 전체리스트 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


print(quick_sort(array))