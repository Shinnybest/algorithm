from collections import deque

def bfs():
    queue = deque([1])
    visited[1] = True
    while queue:
        now = queue.popleft()        
        for move in range(1, 7):
            cur = now + move
            if 1<=cur<=100 and not visited[cur]:
                if cur in ladder.keys():
                    cur = ladder[cur]
                if cur in snake.keys():
                    cur = snake[cur]
                if not visited[cur]:
                    queue.append(cur)
                    visited[cur] = True
                    cnt[cur] = cnt[now] + 1

N, M = map(int, input().split())
ladder = dict()
snake = dict()
for _ in range(N):
    x, y = map(int, input().split())
    ladder[x] = y
for _ in range(M):
    x, y = map(int, input().split())
    snake[x] = y

cnt = [0] * 101
visited = [False] * 101
bfs()
print(cnt[100])