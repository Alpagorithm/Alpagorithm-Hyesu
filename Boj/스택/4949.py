from collections import deque

while True:
    d = deque()

    ans = True
    s = input()
    if s == ".":
        break

    for c in s:
        if c == "(":
            d.append("(")
        elif c == "[":
            d.append("[")
        elif c == ")":
            if len(d) > 0 and d[-1] == "(":
                d.pop()
            else:
                ans = False
                break
        elif c == "]":
            if len(d) > 0 and d[-1] == "[":
                d.pop()
            else:
                ans = False
                break

    if ans and len(d) == 0:
        print("yes")
    else:
        print("no")