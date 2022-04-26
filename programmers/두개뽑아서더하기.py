def solution(numbers):
    answer = set()
    for i in range(0, len(numbers)):
        for j in range(i + 1, len(numbers)):
            sum = numbers[i] + numbers[j]
            answer.add(sum)
    answer = list(answer)
    answer.sort()
    
    return list(answer)

# 다른 사람의 풀이
def solution_1(numbers):
    answer = []
    l = list(combinations(numbers, 2))

    for i in l:
        answer.append(i[0]+i[1])
    answer = list(set(answer))
    answer.sort()

    return answer