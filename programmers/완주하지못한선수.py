import collections

def solution(participant, completion):
    dict = collections.Counter(participant)
    for i in range(len(completion)):
        dict[completion[i]] = dict[completion[i]] - 1
    for key, value in dict.items():
        if value == 1:
            answer = key
            break
    return answer

# 다른 사람의 풀이
def solution_1(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    print(collections.Counter(participant)) # Counter({'mislav': 2, 'stanko': 1, 'ana': 1})
    print(collections.Counter(completion)) # Counter({'stanko': 1, 'ana': 1, 'mislav': 1})
    print(answer) # Counter({'mislav': 1})
    return list(answer.keys())[0]

solution_1(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])