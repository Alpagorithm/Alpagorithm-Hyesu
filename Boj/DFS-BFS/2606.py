from collections import deque

c = int(input())
n = int(input())

data = [[] for _ in range(c+1)]

for i in range(n):
    a, b = map(int, input().split())
    data[a].append(b)
    data[b].append(a)

result = 0

queue = deque()
visited = [False] * (c+1)

queue.append(1)
visited[1] = True
while queue:
    v = queue.popleft()

    for i in data[v]:
        if not visited[i]:
            queue.append(i)
            visited[i] = True
            result += 1

print(result)