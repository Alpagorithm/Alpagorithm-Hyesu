from collections import deque

d = deque()

s = input()
flag = False
ans = 0

for i in s:
    if i == "(":
        flag = True
        d.append(i)
    elif i == ")" and flag == True: # 레이저인경우
        flag = False
        d.pop()
        ans += len(d)
    elif i == ")" and flag == False:
        flag = False
        d.pop()
        ans += 1

print(ans)
