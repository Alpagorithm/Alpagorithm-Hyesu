n = input()
cycle = 0
new = int(n)

while True:

    # 두 자리를 합함
    sum = 0
    for i in str(new):
        sum = sum + int(i)

    # 새로운 수
    new = (new%10 * 10) + sum%10
    cycle = cycle + 1
    if new == int(n):
        break

print(cycle)