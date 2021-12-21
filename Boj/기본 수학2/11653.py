n = int(input())

i = 2
while True:
    if n % i == 0:
        print(i)
        n = n // i
    else:
        i = i + 1
    if i > n:
        break