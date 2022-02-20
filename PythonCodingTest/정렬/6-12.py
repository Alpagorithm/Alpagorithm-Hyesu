n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

for i in range(n):
    print(b[n-1-i])