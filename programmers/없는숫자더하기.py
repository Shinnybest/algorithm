def solution(numbers):
    zero_to_nine = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for number in numbers:
        if number in zero_to_nine:
            zero_to_nine.remove(number)
    
    answer = 0
    
    for i in range(len(zero_to_nine)):
        answer += zero_to_nine[i]
    
    return answer


# 다른 사람의 풀이
def solution_1(numbers):
    return 45 - sum(numbers)