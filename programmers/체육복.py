def solution(n, lost, reserve):
    # new_reserve = [r for r in reserve if r not in lost]
    # new_lost = [l for l in lost if l not in reserve]
    new_reserve = set(reserve) - set(lost)
    new_lost =  set(lost) - set(reserve)
    for r in new_reserve:
        f = r - 1
        b = r + 1
        if f in new_lost:
            new_lost.remove(f)
        elif b in new_lost:
            new_lost.remove(b)
    return n - len(new_lost)