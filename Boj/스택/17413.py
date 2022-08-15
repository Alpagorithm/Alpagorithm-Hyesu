from collections import deque

q = deque()

s = input()
isTag = False

for i in s:
    if i == " " and isTag == False:
        for _ in range(len(q)):
            print(q.pop(), end="")
        print(" ", end="")
    elif i == "<":
        isTag = True
        for _ in range(len(q)):
            print(q.pop(), end="")
        print("<", end="")
    elif i == ">":
        for _ in range(len(q)):
            print(q.popleft(), end="")
        print(">", end="")
        isTag = False
    else:
        q.append(i)

for _ in range(len(q)):
    print(q.pop(), end="")