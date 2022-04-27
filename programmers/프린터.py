from collections import deque

def solution(priorities, location):
    queue = deque([(v,i) for i,v in enumerate(priorities)])
    answer = 0
    while len(queue):
        # pop은 시간 복잡도가 N 이라서 deque를 해서 popleft를 하게 되면 시간복잡도가 1이 되어서 더 유리!
        item = queue.popleft()
        if queue and max(queue)[0] > item[0]:
            queue.append(item)
        else:
            answer += 1
            if item[1] == location:
                break
    return answer

# any를 활용한 다른 사람의 풀이법
def solution_1(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer