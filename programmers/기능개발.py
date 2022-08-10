import math

def solution(progresses, speeds):
    lst = []
    answer = []

    for i in range(len(progresses)):
        days = math.ceil((100 - progresses[i])/speeds[i])
        lst.append(days)
    
    while lst:
        cnt = 1
        for i in range(1, len(lst)):
            if lst[0]>=lst[i]:
                cnt+=1
            else:
                break
        answer.append(cnt)
        lst = lst[cnt:]
    return answer

solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])


def solution2(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]