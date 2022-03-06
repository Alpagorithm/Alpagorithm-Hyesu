n, m = map(int, input().split())
data = []
dp = [-1] * (m+1)
for _ in range(n):
    data.append(int(input()))

for i in data:
    if i <= m:
        dp[i] = 1 # d[2] = 1, d[5] = 1

for i in range(1, m+1):
    if dp[i] != -1:
        continue

    for j in data:
        # 계산 가능한지 체크
        if i-j > 0 and dp[i-j] == -1:
            continue
        if i-j > 0:
            dp[i] = dp[i-j] + 1

print(dp[m])