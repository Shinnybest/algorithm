def solution(absolutes, signs):
    answer = 0
    while len(absolutes) > 0:
        if signs[0]:
            answer += absolutes[0]
        else:
            answer -= absolutes[0]
        signs.pop(0)
        absolutes.pop(0)
    return answer