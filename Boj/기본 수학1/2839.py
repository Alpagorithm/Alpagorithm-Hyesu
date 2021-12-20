n = int(input())
list = []
a = 0
isTrue = False
while 5*a <= n:
    b = (n-5*a) % 3
    if b == 0:
        list.append(a+((n-5*a) // 3))
        isTrue = True
    a = a + 1

if isTrue == False:
    print(-1)
    exit(0)

min = list[0]
for i in range(len(list)):
    if list[i] < min:
        min = list[i]
print(min)