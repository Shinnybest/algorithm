def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command
        answer.append(array[i-1:j][k-1])
    return answer