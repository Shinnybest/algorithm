def solution(dartResult):
    number = []
    temp_num = ""
    for i in range(len(dartResult)):
        if dartResult[i] == "S":
            number.append(int(temp_num))
            temp_num = ""
        elif dartResult[i] == "D":
            number.append(int(temp_num)*int(temp_num))
            temp_num = ""
        elif dartResult[i] == "T":
            number.append(int(temp_num)*int(temp_num)*int(temp_num))
            temp_num = ""
        elif dartResult[i] == "*":
            if len(number) < 2:
                number[-1] = number[-1] * 2
            else:
                number[-1] = number[-1] * 2
                number[-2] = number[-2] * 2
        elif dartResult[i] == "#":
            number[-1] = number[-1] * (-1)
        else:
            temp_num += dartResult[i]
    
    return sum(number)

# 다른 사람의 풀이
def solution(dartResult):
    point = []
    answer = []
    dartResult = dartResult.replace('10','k')
    point = ['10' if i == 'k' else i for i in dartResult]
    print(point)

    i = -1
    sdt = ['S', 'D', 'T']
    for j in point:
        if j in sdt :
            answer[i] = answer[i] ** (sdt.index(j)+1)
        elif j == '*':
            answer[i] = answer[i] * 2
            if i != 0 :
                answer[i - 1] = answer[i - 1] * 2
        elif j == '#':
            answer[i] = answer[i] * (-1)
        else:
            answer.append(int(j))
            i += 1
    return sum(answer)

import re


def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer