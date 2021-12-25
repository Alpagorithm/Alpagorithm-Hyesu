n = int(input())

def d(a):
    if a == 0:
        return 0
    elif a == 1:
        return 1
    else:
        return d(a-1) + d(a-2)

print(d(n))