def solution(numbers, target):
    answer = 0

    def dfs(depth, sum):
        if depth == len(numbers) - 1:
            if sum == target:
                nonlocal answer
                answer += 1
            return
        dfs(depth + 1, sum + numbers[depth + 1])
        dfs(depth + 1, sum - numbers[depth + 1])

    dfs(-1, 0)

    return answer