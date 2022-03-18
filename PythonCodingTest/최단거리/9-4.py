INF = int(1e9)

n, m = map(int, input().split())

# 2차원 리스트 만들고, 모든 값을 무한으로 초기화한다.
graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

# 알고리즘 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 결과 출력
ans = graph[1][k] + graph[k][x]
if ans >= INF:
    print(-1)
else:
    print(ans)
