def solution(s):
    if len(s) == 1:
        return 1
            
    answer_list = []
    
    for i in range(1, (len(s)//2)+1):
        prev = s[0:i]
        cnt = 1
        answer = ''
        for j in range(i, len(s), i):
            cur = s[j:j+i]
            if prev == cur:
                cnt+=1
            else:
                if cnt != 1:
                    answer = answer + str(cnt) + prev
                else:
                    answer = answer + prev
                prev = cur
                cnt = 1
        if cnt != 1:
            answer = answer + str(cnt) + prev
        else:
            answer = answer + prev
        answer_list.append(len(answer))
    
    return min(answer_list)