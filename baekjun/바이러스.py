def solution(n, m):
    graph = [[] for _ in range(n+1)]
    computers = [[1, 2], [2, 3], [1, 5], [5, 2], [5, 6], [4, 7]]

    for _ in range(m):
        a,b = computers.pop()
        graph[a].append(b)
        graph[b].append(a)
        
    cnt = 0
    visited = [0]*(n+1)
    def dfs(start):
        nonlocal cnt
        visited[start] = 1
        print(graph[start])
        for i in graph[start]:
            if visited[i]==0:
                dfs(i)
                cnt +=1

    dfs(1)
    print(cnt)
    return cnt

solution(7, 6)