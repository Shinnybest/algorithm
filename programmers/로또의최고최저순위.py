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

# 다른 사람의 풀이, index, count
def solution_1(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]

def solution_2(lottos, win_nums):
    rank = {
        0: 6,
        1: 6,
        2: 5,
        3: 4,
        4: 3,
        5: 2,
        6: 1
    }
    return [rank[len(set(lottos) & set(win_nums)) + lottos.count(0)], rank[len(set(lottos) & set(win_nums))]]