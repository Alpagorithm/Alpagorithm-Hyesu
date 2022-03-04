# 피보나치 수열 소스코드 (재귀, 메모이제이션 사용)

d = [0] * 100 # 저장공간

def fibo(x):
    if x == 1 or x == 2:
        return 1
    # 이미 계산한 적 있는 문제의 경우
    if d[x] != 0:
        return d[x]
    # 아직 계산하지 않는 문제의 경우
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(99))