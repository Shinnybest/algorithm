from collections import deque

H, W = map(int, input().split())
island = [list(map(str, input())) for _ in range(H)]
visited = [[False] * W for _ in range(H)]
dir = [(1, 0), (-1, 0), (0, -1), (0, 1)]

def bfs(s, e, dist):
    q = deque([(s, e, dist)])
    max = -1
    visited[s][e] = True
    while q:
        y, x, c = q.popleft()
        if max < c:
            max = c
        for i in range(4):
            ny = y + dir[i][0]
            nx = x + dir[i][1]
            if 0<=ny<H and 0<=nx<W and not visited[ny][nx] and island[ny][nx] == 'L':
                q.append((ny, nx, c+1))
                visited[ny][nx] = True
    return max

Max = -1
for i in range(H):
    for j in range(W):
        if island[i][j] == 'L':
            visited = [[False] * W for _ in range(H)]
            Max = max(Max, bfs(i, j, 0))

print(Max)