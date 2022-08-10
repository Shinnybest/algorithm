from collections import defaultdict

def solution_defaultdict(clothes):
    
    dict = defaultdict(list)
    for i in range(len(clothes)):
        dict[clothes[i][1]].append(clothes[i][0])
    answer = 1
    for key, value in dict.items():
        answer *= (len(value)+1)
    return answer-1

solution_defaultdict([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])


def solution_hash(clothes):
    clothes_type = {}

    for c, t in clothes:
        if t not in clothes_type:
            clothes_type[t] = 2
        else:
            clothes_type[t] += 1

    cnt = 1
    for num in clothes_type.values():
        cnt *= num

    return cnt - 1