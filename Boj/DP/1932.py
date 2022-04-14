n = int(input())
data = []
dp = [[0] * n for _ in range(n)]
answer = 0

def max_sum(a, b):
    if dp[a][b] != 0:
        return dp[a][b]
    if a == n-1:
        dp[a][b] = data[a][b]
    else:
        dp[a][b] = data[a][b] + max(max_sum(a+1, b), max_sum(a+1, b+1))
    return dp[a][b]


for i in range(n):
    data.append(list(map(int, input().split())))

print(max_sum(0, 0))
