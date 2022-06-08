def solution(gems):
    start, end = 0, 0
    length = [0, 0, 100001]
    t = len(set(gems))
    dict = {}
    while end<len(gems):
        if start == len(gems)-t or length[2] == t:
            break
        if len(dict) == t:
            dist = end-start+1
            if dist < length[2]:
                length = [start, end, dist]
            start += 1
        else:
            end += 1
            dict[gems[end]] = end
        
    print([length[0]+1, length[1]+1])
    
solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])