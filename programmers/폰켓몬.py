def solution1(nums):
    answer = len(set(nums))
    if answer > len(nums) // 2:
        answer = len(nums) // 2
    return answer


def solution2(nums):
    choose = len(nums)/2
    types = len(set(nums))
    if types >= choose:
        return choose
    else:
        return types