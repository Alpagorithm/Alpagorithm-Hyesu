n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

for i in range(k):
    if a[i] < b[n-1-i]:
        a[i], b[n-1-i] = b[n-1-i], a[i]
    else:
        break

print(sum(a))