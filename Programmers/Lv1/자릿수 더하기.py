def solution(n):
    answer = 0
    data = str(n)
    for d in data:
        answer += int(d)
    return answer