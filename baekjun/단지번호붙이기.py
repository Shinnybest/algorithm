from collections import deque

N = int(input())
village = [list(map(int, input())) for _ in range(N)]
visited = [[False] * N for _  in range(N)]
dir = [(1, 0), (-1, 0), (0, -1), (0, 1)]

def bfs(y, x):
    q = deque([(y, x)])
    cnt = 0
    while q:
        s, e = q.popleft()
        cnt += 1
        for i in range(4):
            ns = s + dir[i][0]
            ne = e + dir[i][1]
            if 0<=ns<N and 0<=ne<N and not visited[ns][ne]:
                visited[ns][ne] = True
                if village[ns][ne] == 1:
                    q.append((ns, ne))
    return cnt

answer = []

for i in range(N):
    for j in range(N):
        if not visited[i][j] and village[i][j] == 1:
            visited[i][j] = True
            answer.append(bfs(i, j))

print(len(answer))         
for cnt in sorted(answer):
    print(cnt)