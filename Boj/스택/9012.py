t = int(input())

for i in range(t):
    stack = []
    ans = True
    data = input()
    for k in data:
        if k == "(":
            stack.append(k)
        else:
            if len(stack) > 0:
                stack.pop()
            else:
                ans = False
                break

    if len(stack) > 0:
        ans = False

    if ans:
        print("YES")
    else:
        print("NO")