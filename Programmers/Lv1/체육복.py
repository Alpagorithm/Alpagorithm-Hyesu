def solution(n, lost, reserve):
    # 1. 중복 원소 제거
    lost_student = set(lost) - set(reserve)
    reserve_student = set(reserve) - set(lost)

    n -= len(lost_student)

    for r in reserve_student:
        if r - 1 in lost_student:
            lost_student.remove(r - 1)
            n += 1
            continue
        if r + 1 in lost_student:
            lost_student.remove(r + 1)
            n += 1

    return n