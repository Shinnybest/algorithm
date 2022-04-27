# https://velog.io/@younge/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%94%94%EC%8A%A4%ED%81%AC-%EC%BB%A8%ED%8A%B8%EB%A1%A4%EB%9F%AC-%ED%9E%99

import heapq

def solution(jobs):
    
    heapq.heapify(jobs)
    
    total = [jobs[0][0], jobs[0][1], jobs[0][1] - jobs[0][0], jobs[0][1]]
    
    for i in range(1, len(jobs)):
        start = jobs[i][0]
        run = jobs[i][1]
        end = total[i-1][2] + jobs[i][1]
        spend = total[i-1][2] - jobs[i][0] + jobs[i][1]
        total.append([start, run, end, spend])
        
    
    
    all_time = 0
    
    for i in range(len(total)):
        all_time += total[i][3]
        
    return all_time / len(total)