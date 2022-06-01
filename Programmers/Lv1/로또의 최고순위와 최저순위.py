def solution(lottos, win_nums):
    data = list(set(lottos).intersection(win_nums))
    rank = [6, 6, 5, 4, 3, 2, 1]  # index가 맞은 개수, 내용은 등수 (ex. 0개맞으면 -> rank[0] -> 6등!)

    answer = [rank[len(data) + lottos.count(0)], rank[len(data)]]
    return answer