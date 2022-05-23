import sys
N, M = map(int, sys.stdin.readline().strip().split())
s = []
def dfs():
    if len(s)==M:
        print(' '.join(map(str,s)))
        return
    
    for i in range(1,N+1):
        # if i not in s:
        s.append(i)
        dfs()
        s.pop()
dfs()
# 216ms, 