# 1st 72ms 30840kb
# from itertools import combinations
import sys

# N, M = map(int, sys.stdin.readline().strip().split())
# # N, M = 8, 3
# lst = [str(i) for i in range(1, N+1)]
# answers = list(combinations(lst, M))

# for item in answers:
#     print(" ".join(item))

# 2nd 68ms 30840kb
N, M = map(int, sys.stdin.readline().strip().split())
lst = [str(i) for i in range(1, N+1)]
answers = []
def dfs(start):
    if len(answers) == M:
        print(' '.join(map(str, answers)))
        return
    for i in range(start, N+1):
        answers.append(i)
        dfs(i+1)
        answers.pop()
dfs(1)
