def solution(a, b):
    answer = 0
    length = len(a)
    for i in range(length):
        answer += a[i] * b[i]
    return answer

# 다른 사람의 풀이
# zip
def solution_1(a, b):

    return sum([x*y for x, y in zip(a,b)])