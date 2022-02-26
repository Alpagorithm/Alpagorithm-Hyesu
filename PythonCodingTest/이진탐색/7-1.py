# 순차탐색
def sequential_search(n, target, array):
    for i, num in enumerate(array, start=1):
        if num == target:
            return i

print("생성할 원소 개수를 입력한 다음 한칸 띄고 찾을 문자열을 입력하세요.")
n, target = input().split()
n = int(n)

print("앞서 작은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")
array = input().split()

print(sequential_search(n, target, array))