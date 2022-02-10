# 재귀함수 - 종료조건을 항상 명시해야 한다.
# 재귀함수는 컴퓨터 내부에서 스택 자료구조를 이용하여 실행된다.

# 100번째 종료됨
def recursive_function(i):
    if i == 100:
        return
    recursive_function(i+1)
    print(i)

recursive_function(20)