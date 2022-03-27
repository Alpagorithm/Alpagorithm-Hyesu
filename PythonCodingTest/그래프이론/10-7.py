# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b - find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v+1)

# 부모 테이블 상에서, 부모를 자기 자신으로 초기화하기
for i in range(1, v+1):
    parent[i] = i

for i in range(e):
    sol, a, b = map(int, input().split())
    if sol == 0:
        # 팀합치기
        union_parent(parent, a, b)
    elif sol == 1:
        # 같은 팀 소속인지 확인
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")
