n, x = map(int, input().split())
number = list(map(int, input().split()))

for i in range(0, n):
    if number[i] < x:
        print(number[i], end= " ")