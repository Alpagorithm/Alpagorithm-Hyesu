# 2019 카카오 겨울 인턴십 Level 1

def solution(board, moves):
    answer = 0
    stack = []

    for move in moves:
        move -= 1
        for i in range(len(board)):
            if board[i][move] > 0:
                v = board[i][move]
                board[i][move] = 0
                stack.append(v)
                if len(stack) > 1:
                    if stack[-2] == stack[-1]:
                        answer += 2
                        stack.pop()
                        stack.pop()
                break
    return answer