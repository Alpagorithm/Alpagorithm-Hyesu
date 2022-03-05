x = int(input())

d = [0] * 30001

for i in range(2, x+1):
    # 조건들
    d[i] = d[i-1] + 1
    if i % 2 == 0:
        d[]