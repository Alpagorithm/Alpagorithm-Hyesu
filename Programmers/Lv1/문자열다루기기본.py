def solution(s):
    answer = s.isdigit() and (len(s) == 4 or len(s) == 6)
    return answer