import math

def solution(numbers, hand):
    answer = ''
    t_arr = [[0, 0], [1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3], [4, 1], [4, 2], [4, 3]]
    l_arr = ["10"]
    r_arr = ["12"]
    for x in range(len(numbers)):
        if numbers[x] in [1, 4, 7]:
            answer += "L"
            l_arr.append(numbers[x])
        elif numbers[x] in [3, 6, 9]:
            answer += "R"
            r_arr.append(numbers[x])
        elif numbers[x] in [2, 5, 8, 0]:
            if numbers[x] == 0:
                numbers[x] = 11
            if abs(t_arr[int(l_arr[-1])][0] - t_arr[numbers[x]][0]) + abs(t_arr[int(l_arr[-1])][1] - t_arr[numbers[x]][1]) > abs(t_arr[int(r_arr[-1])][0] - t_arr[numbers[x]][0]) + abs(t_arr[int(r_arr[-1])][1] - t_arr[numbers[x]][1]):
                answer += "R"
                r_arr.append(numbers[x])
            elif abs(t_arr[int(l_arr[-1])][0] - t_arr[numbers[x]][0]) + abs(t_arr[int(l_arr[-1])][1] - t_arr[numbers[x]][1]) < abs(t_arr[int(r_arr[-1])][0] - t_arr[numbers[x]][0]) + abs(t_arr[int(r_arr[-1])][1] - t_arr[numbers[x]][1]):
                answer += "L"
                l_arr.append(numbers[x])
            elif abs(t_arr[int(l_arr[-1])][0] - t_arr[numbers[x]][0]) + abs(t_arr[int(l_arr[-1])][1] - t_arr[numbers[x]][1]) == abs(t_arr[int(r_arr[-1])][0] - t_arr[numbers[x]][0]) + abs(t_arr[int(r_arr[-1])][1] - t_arr[numbers[x]][1]):
                answer += hand[0].upper()
                if hand == "right":
                    r_arr.append(numbers[x])
                else:
                    l_arr.append(numbers[x])
    
    return answer

# 다른 사람의 풀이
def solution_1(numbers, hand):
    answer = ''
    key_dict = {1:(0,0),2:(0,1),3:(0,2),
                4:(1,0),5:(1,1),6:(1,2),
                7:(2,0),8:(2,1),9:(2,2),
                '*':(3,0),0:(3,1),'#':(3,2)}

    left = [1,4,7]
    right = [3,6,9]
    lhand = '*'
    rhand = '#'
    for i in numbers:
        if i in left:
            answer += 'L'
            lhand = i
        elif i in right:
            answer += 'R'
            rhand = i
        else:
            curPos = key_dict[i]
            lPos = key_dict[lhand]
            rPos = key_dict[rhand]
            ldist = abs(curPos[0]-lPos[0]) + abs(curPos[1]-lPos[1])
            rdist = abs(curPos[0]-rPos[0]) + abs(curPos[1]-rPos[1])

            if ldist < rdist:
                answer += 'L'
                lhand = i
            elif ldist > rdist:
                answer += 'R'
                rhand = i
            else:
                if hand == 'left':
                    answer += 'L'
                    lhand = i
                else:
                    answer += 'R'
                    rhand = i

    return answer