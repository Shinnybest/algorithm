from collections import deque

def solution(N, M):
    list = [i for i in range(1, N+1)]
    queue = deque(list)
    result = []
    
    while queue:
        for _ in range(M):
            popped = queue.popleft()
            queue.append(popped)
        result.append(queue.pop())
    return result

solution(7, 3)