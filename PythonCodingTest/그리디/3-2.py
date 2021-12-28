n, m, k = map(int, input().split())
list = list(map(int, input().split()))

# 주어진 수를 m번 더하는데 특정한 인덱스의 수가
list.sort()
# print(list)

max = list[n-1]
maxNext = list[n-2]

ans = 0
k = 0
for i in range(0, m):
    if k == 3:
        # print(i)
        ans = ans + maxNext
        k = 0
    else:
        ans = ans + max
        k = k + 1

print(ans)