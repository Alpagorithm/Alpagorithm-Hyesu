h, m = input().split()
h = int(h)
m = int(m)

if m-45<0 and h-1<0:
    print(23, 60+m-45)
elif m-45<0 and h-1>=0:
    print(h-1, m+60-45)
else:
    print(h, m-45)