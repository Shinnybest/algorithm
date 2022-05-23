Total = int(input())
for _ in range(Total):
    N, M, S = map(int, input().split())
    lst = [[0] * N for _ in range(M)]
    for i in range(S):
        y, x = map(int, input().split())
        lst[y][x] = 1

    cnt = 0
    def dfs(i, j):
        if lst[i][j] == 0:
            return
        else:
            dx = [1, -1, 0, 0]
            dy = [0, 0, 1, -1]
            lst[i][j] = 0
            for z in range(4):
                i = i + dx[z]
                j = j + dy[z]
                if 0<=i<=M-1 and 0<=j<=N-1:
                    dfs(i, j)

    for i in range(M):
        for j in range(N):
            if lst[i][j] == 1:
                dfs(i, j)
                cnt += 1
    print(cnt)