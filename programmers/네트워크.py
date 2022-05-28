# 1st dfs 방식
def dfs(n, computers, i, visited):
    visited[i] = True
    for z in range(n):
        if z!=i and computers[i][z]==1:
            if visited[z] ==False:
                dfs(n, computers, z, visited)
    
def solution(n, computers):
    cnt = 0
    visited = [False for _ in range(n)]
    for i in range(n):
        if visited[i] == False:
            dfs(n, computers, i, visited)
            cnt += 1
    return cnt

# 2nd bfs
def solution(n, computers):
    cnt = 0
    visited = [0 for _ in range(n)]
    
    def bfs(num):
        queue = []
        queue.append(num)
        while len(queue) != 0:
            visited[num] = 1
            num = queue.pop(0)
            for i in range(n):
                if computers[num][i] and visited[i]==0:
                    queue.append(i)

    for i in range(n):
        if visited[i] == 0:
            bfs(i)
            cnt += 1
    return cnt