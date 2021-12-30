def solution(n, lost, reserve):
    lostReal = set(lost) - set(reserve)
    reserveReal = set(reserve) - set(lost)

    for r in reserveReal:
        if r - 1 in lostReal:
            lostReal.remove(r - 1)
        elif r + 1 in lostReal:
            lostReal.remove(r + 1)
    return n - len(lostReal)