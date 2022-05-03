def solution(stones, k):
    stones.sort()
    left = 1
    right = max(stones)
    while left + 1 < right:
        mid = (left + right) // 2
        if mid<=k:
            left = mid
        else:
            right = mid

    return stones.index(left) + 1

solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3)