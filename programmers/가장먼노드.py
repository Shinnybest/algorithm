def solution(n, vertex):
    graph = [[0]*(n+1) for i in range(n+1)]
    for i in range(n+1):
        l = vertex[i][0]
        r = vertex[i][1]
        graph[l][r], graph[r][l] = 1, 1

    max_val = float('inf')

    visited = [max_val] * (n+1)

    def bfs(num, cnt):
        graph[cnt][num] = 0
        queue = []
        queue.append(num)
        while len(queue):
            num = queue.pop(0)
            visited[num] = min(cnt, visited[num])
            for i in range(n+1):
                if graph[num][i] == 1:
                    graph[i][num] = 0
                    queue.append(i)
            cnt +=1
            
    for i in range(1, n+1):
        if graph[1][i]==1:
            bfs(i, 1)

    answer = []
    visited = sorted(visited, reverse=True)[1:]
    for i in range(len(visited)):
        if visited[i] == max(visited):
            answer.append(visited[i])
        else:
            break
    return len(answer)


solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])