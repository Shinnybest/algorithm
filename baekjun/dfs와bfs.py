from collections import defaultdict, deque

N, M, V = map(int, input().split())
dict = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    dict[a].append(b)
    dict[b].append(a)

for i in range(1, N+1):
    dict[i].sort()

answer = []

def dfs(num):
    if num in answer:
        return
    answer.append(num)
    print(num, end=' ')
    for i in dict[num]:
        dfs(i)

dfs(V)


def bfs(start):
    q = deque([start])
    answer = [start]
    
    print(start, end=' ')
    while q:
        n = q.popleft()
        for num in dict[n]:
            if num not in answer:
                answer.append(num)
                print(num, end=' ')
                q.append(num)
    return answer
print()
bfs(V)