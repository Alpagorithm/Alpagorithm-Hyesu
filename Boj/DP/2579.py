n = int(input())
scores = []
dp = [0] * (n+1)

for _ in range(n):
    scores.append(int(input()))

for i in range(len(scores)):
    if i == 0:
        dp[0] = scores[0]
        continue
    if i == 1:
        dp[1] = scores[1] + dp[0]
        continue
    if i == 2:
        dp[2] = max(scores[0], scores[1]) + scores[2]

    dp[i] = max(scores[i-1] + dp[i-3], dp[i-2]) + scores[i]

print(dp[n-1])