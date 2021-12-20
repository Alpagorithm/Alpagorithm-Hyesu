a, b, c = map(int, input().split())

result = 0

if a + (b - c) * 2 >= a + b - c:
    result = -1
    print(result)
else:
    result = a//(c - b) + 1
    print(result)
