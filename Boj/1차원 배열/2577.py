a = int(input())
b = int(input())
c = int(input())

number = []
answer = []

for i in str(a*b*c):
    number.append(int(i))

for i in range(0, 10):
    answer.append(0)

for i in number:
    answer[i] = answer[i] + 1

for i in range(0, 10):
    print(answer[i])