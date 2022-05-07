def solution(skill, skill_trees):
    
    answer = 0
    for tree in skill_trees:
        skill_list = list(skill)
        for i in tree:
            if i in skill_list:
                if i != skill_list.pop(0):
                    break
        else:
            answer += 1

    return answer

solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"])
