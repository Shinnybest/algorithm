from collections import deque 

# solution 1 -> stack
def solution1(cacheSize, cities):
    q = []
    answer = 0
    
    for city in cities:
        city = city.lower()
        if city in q:
            answer += 1
            # idx = q.index(city)
            # q.pop(idx)
            q.remove(city)
            q.append(city)
        else:
            answer +=5
            if cacheSize !=0:
                if len(q) == cacheSize:
                    q.pop(0)
                q.append(city)
    return answer

# solution2 -> queue
def solution2(cacheSize, cities):
    q = deque()
    # q = []
    answer = 0
    
    for city in cities:
        city = city.lower()
        if city in q:
            answer += 1
            q.remove(city)
            q.append(city)
        else:
            answer +=5
            if cacheSize !=0:
                if len(q) == cacheSize:
                    q.popleft()
                q.append(city)
    return answer