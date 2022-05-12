def solution(s):
    s = (s[1:-1] + ",").split("},")[:-1]
    dict = {}
    for i in range(len(s)):
        split_nums = s[i][1:].split(",")
        dict[len(split_nums)] = split_nums
    
    prev = []
    answer = []
    
    for i in range(1, len(s)+1):
        for num in dict[i]:
            if num not in prev:
                answer.append(int(num))
                break
        prev = dict[i]
    return answer