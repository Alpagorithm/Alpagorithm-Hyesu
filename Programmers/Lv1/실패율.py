def solution(N, stages):
    n = N
    dic = {}
    sum = len(stages)
    for i in range(1, n + 1):

        if sum != 0:
            dic[i] = stages.count(i) / sum
        else:
            dic[i] = 0
        sum = sum - stages.count(i)

    return sorted(dic, key=lambda x: dic[x], reverse=True)