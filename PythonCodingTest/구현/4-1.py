n = int(input())
data = list(input().split())
print(data)
x = 1
y = 1

for i in data:
    if i == 'L':
        if x > 1:
            x = x-1
    elif i == 'R':
        if x < n:
            x = x + 1
    elif i == 'U':
        if y > 1:
            y = y-1
    elif i == 'D':
        if y < n:
            y = y +1

print(y, x)
