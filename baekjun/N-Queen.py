# N = int(input())
N = 8

chess = [[0] * N for _ in range(N)]
cnt = 0

def is_promising(x, y, current):
    if current[x][y] != 1:
        for i in range(N):
            current[i][y] = 1
        if x+1 <= N-1:
            current[x+1][y] = 1
        if (x+1 <= N-1) and (y+1 <= N-1):
            current[x+1][y+1] = 1
        if (x+1 <= N-1) and (y-1 >= 0):    
            current[x+1][y-1] = 1
        return current
    return False

def dfs(x, current):
    if x == N:
        global cnt
        cnt += 1
        return
    else:
        for z in range(N):
            A = is_promising(x, z, current)
            if A:
                dfs(x+1, A)
    
dfs(0, chess)
print(cnt)