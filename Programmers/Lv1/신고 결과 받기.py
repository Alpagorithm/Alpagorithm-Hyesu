def solution(id_list, report, k):
    answer = []
    reports = set(report)
    reported_count = {}
    reported_id = {}

    for id in id_list:
        reported_count[id] = 0
        reported_id[id] = []

    for report in reports:
        a, b = report.split()
        reported_id[a].append(b)
        reported_count[b] += 1

    filtered = dict(filter(lambda elem: elem[1] >= k, reported_count.items()))
    filtered_id = list(filtered.keys())

    for key, value in reported_id.items():
        answer.append(len(set(value) & set(filtered_id)))

    return answer