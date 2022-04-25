def solution(lottos, win_nums):
    same = 7
    
    for i in range(0, 6):
            if win_nums[i] in lottos:
                same -= 1
            
    if 0 in lottos:
        zero_cnt = lottos.count(0)
        h_rank = same - zero_cnt
        if same == 7:
            same = 6
        answer = [h_rank, same]
        
    else:
        if same == 7:
            same = 6
        answer = [same, same]
        
    return answer