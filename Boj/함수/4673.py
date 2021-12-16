def d(n):
    result = n
    for i in str(n):
        result = result + int(i)
    return result

ans = []

# ans = [1, 2, 3, ...]
for i in range(0, 10000):
    ans.append(i+1)


for i in range(1, 10000):
    k = d(i)
    if k > 10000:
        continue
    else:
        ans[k-1] = 0

# 정답 출력
for i in ans:
    if i != 0:
        print(i)