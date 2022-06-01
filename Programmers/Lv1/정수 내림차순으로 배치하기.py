def solution(n):
    answer = 0
    n = list(map(int, str(n)))
    n.sort(reverse=True)
    answer = int(''.join(map(str, n)))
    return answer