a, b = map(int, input().split())

a = (a % 10)*100 + (a//10%10) * 10 + (a//100)
b = (b % 10)*100 + (b//10%10) * 10 + (b//100)

if a > b:
    print(a)
else:
    print(b)