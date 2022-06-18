from collections import deque

N = int(input())
sy, sx, ey, ex = map(int, input().split())

graph = [[-1] * N for _ in range(N)]
move = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]

def bfs(y, x):
    q = deque()
    q.append((y, x))
    graph[y][x] = 0 
    while q:
        ny, nx = q.popleft()
        for i in range(len(move)):
            yy = ny+move[i][0]
            xx = nx+move[i][1]
            if 0<=yy<N and 0<=xx<N and graph[yy][xx] == -1:
                q.append((yy, xx))
                graph[yy][xx] = graph[ny][nx] + 1

bfs(sy, sx)
print(graph[ey][ex])