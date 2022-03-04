d = [0] * 100 # DP테이블

d[1] = 1
d[2] = 1
n = 99

for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2] # DP테이블 배열에 저장

print(d[n])