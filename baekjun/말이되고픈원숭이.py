from collections import deque

K = int(input())
W, H = map(int, input().split())

horse = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1), (2, 1), (1, 2)]
monkey = [(-1, 0), (1, 0), (0, -1), (0, 1)]
board = [list(map(int, input().split())) for _ in range(H)]
visited = [[False]*W for _ in range(H)]
dist = [[0] * W for _ in range(H)]

def move_like_horse(cnt):
    if cnt == 0:
        return
    q = deque([(0, 0)])
    while cnt > 0 and q:
        y, x = q.popleft()
        for i in range(8):
            ny = y + horse[i][0]
            nx = x + horse[i][1]
            if 0<=ny<H and 0<=nx<W and board[ny][nx] == 1:
                if y < ny:
                    ny = ny + 1
                elif y > ny:
                    ny = ny - 1
                if x < nx:
                    nx = nx + 1
                elif x > nx:
                    nx = nx - 1
            # 사방위 움직임까지 체크해야함
            if 0<=ny<H and 0<=nx<W and not visited[ny][nx]:
                visited[ny][nx] = True
                q.append((ny, nx))
        cnt -= 1
    return q

r = move_like_horse(K)

if len(r) == 0:
    print(-1)
else:
    for y, x in r:
        dist[y][x] = K

    print("dist", dist)

    answer = 1e9

    def move_like_monkey(queue):
        global answer
        queue = deque(queue)
        while queue:
            y, x = queue.popleft()
            if y == H-1 and x == W-1:
                answer = min(answer, dist[y][x])
            else:
                for d in range(4):
                    ny = y + monkey[d][0]
                    nx = x + monkey[d][1]
                    if 0<=ny<H and 0<=nx<W and not visited[ny][nx] and board[ny][nx] == 0:
                        visited[ny][nx] = True
                        dist[ny][nx] = dist[y][x] + 1
                        queue.append((ny, nx))

    move_like_monkey(r)

    print("answer : ", answer)

    if answer == 1e9:
        print("갈 수가 없다면 : ", -1)