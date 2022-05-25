def solution(numbers):
    answer = []

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            k = numbers[i] + numbers[j]
            if k not in answer:
                answer.append(k)

    answer.sort()
    return answer