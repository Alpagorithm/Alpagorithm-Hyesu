t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())
    x = 0
    # n = h*y+x
    while n > h * x:
        x = x + 1

    y = n - h * (x - 1)
    x = str(x).zfill(2)
    y = str(y)
    print("%s%s" % (y, x))