import sys
input = sys.stdin.readline
n = int(input())

stack = []
for i in range(n):
    d = list(input().split())
    if d[0] == "push":
        stack.append(d[1])
    elif d[0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif d[0] == "size":
        print(len(stack))
    elif d[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif d[0] == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
