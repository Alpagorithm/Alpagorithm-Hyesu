n, k = map(int, input().split())
list = []
for i in range(n):
    list.append(int(input()))

list.sort(reverse=True)

ans = 0
for i in list:
    ans += k//i
    k = k % i

print(ans)