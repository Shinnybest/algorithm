from collections import deque

N, M, V = map(int, input().split())

graph = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    m1, m2 = map(int, input().split())
    graph[m1][m2] = graph[m2][m1] = 1

result = [V]

def bfs(start):
    queue = deque()
    discovered = []
    for i in range(N+1):
        if graph[start][i] == 1:
            queue.append(graph[start][i])
    while queue:
        discovered.append(queue.popleft())
    result.append(discovered)
    for i in range(len(discovered)):
        bfs(discovered[i])


def dfs(start, discovered = []):
    discovered.append(start)
    for i in range(N+1):
        if graph[start][i] == 1 and graph[start][i] not in discovered:
            dfs(graph[start][i])