def solution(number, k):
    answer = ''
    stack = []

    for n in number:

        while len(stack) > 0 and stack[-1] < n and k > 0:
            stack.pop()
            k -= 1
        stack.append(n)

    answer = "".join(stack)

    # 입력값이 "99991", 3인경우 처리해줘야함
    if len(answer) > len(number) - k:
        answer = answer[0:len(number) - k]

    return answer