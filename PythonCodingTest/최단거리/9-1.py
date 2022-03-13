import sys
input = sys.stdin.readline
INF = int(1e9) # 10억

# 노드의 개수, 간선의 개수를 입력받는다.
n, m = map(int, input().split())
# 시작 노드를 입력받는다.
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만든다
graph = [[] for i in range(n+1)]
# 방문한 적이 있는지 체크하는 리스트를 만든다.
visited = [False] * (n+1)
# 최단 거리 테이블을 모두 무한으로 초기화한다.
distance = [INF] * (n+1)

# 모든 간선의 정보를 입력받는다.
for _ in range(m):
    a, b, c = map(int, input().split())
    # a 노드에서 b 노드로 가는 비용이 c다.
    graph[a].append((b,c))

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 ㅓㄴ호를 반환
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # 시작노드에 대해 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now]+j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    if distance[i] == INF:
        print("InFINITY")
    else:
        print(distance[i])