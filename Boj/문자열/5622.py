w = input()
ans = 0

for i in w:
    if i <= 'C':
        ans = ans + 3
    elif i <= 'F':
        ans = ans + 4
    elif i <= 'I':
        ans = ans + 5
    elif i <= 'L':
        ans = ans + 6
    elif i <= 'O':
        ans = ans + 7
    elif i <= 'S':
        ans = ans + 8
    elif i <= 'V':
        ans = ans + 9
    else:
        ans = ans + 10

print(ans)