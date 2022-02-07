n = int(input())
ans = 0
# 00시 00분 00초~ 00시 59분 59초 1 2
for i in range(n+1):
    if i == 3 or i == 13 or i == 23:
        ans += 3600
    else:
        ans += 1575
print(ans)