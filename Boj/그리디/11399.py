n = int(input())
list = list(map(int, input().split()))

list.sort(reverse=True)
ans = 0

for i in range(len(list)):
    ans = ans + list[i] * (i+1)

print(ans)