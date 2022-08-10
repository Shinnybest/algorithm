import collections

def solution1(participant, completion):
    dict = collections.Counter(participant)
    for i in range(len(completion)):
        dict[completion[i]] -= 1
    for key, value in dict.items():
        if value == 1:
            answer = key
            break
    return answer

# 다른 사람의 풀이
def solution2(participant, completion):
    dict = collections.Counter(participant) - collections.Counter(completion)
    return list(dict.keys())[0]