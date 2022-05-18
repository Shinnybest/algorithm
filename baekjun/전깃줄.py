# 1st Trial
# import sys
# input = sys.stdin.readline

# N = int(input())
# lst = []

# for _ in range(N):
#     lst.append(list(map(int, input().split())))

# intersection_cnt = 0
# answer = 0
# for i in range(N-1):
#     for j in range(i+1, N):
#         if (lst[i][0]<lst[j][0] and lst[i][1]>lst[j][1]) or (lst[i][0]>lst[j][0] and lst[i][1]<lst[j][1]):
#             intersection_cnt += 1
# while intersection_cnt > 0:
#     max_num = []
#     for idx, i in enumerate(lst):
#         cnt = 0
#         for j in lst:
#             if (i[0]<j[0] and i[1]>j[1]) or (i[0]>j[0] and i[1]<j[1]):
#                 cnt += 1
#         if len(max_num) == 0 or max_num[0][1] < cnt:
#             max_num.append([idx, cnt])
#     intersection_cnt -= max_num[0][1]
#     lst.pop(idx)
#     answer += 1
# print(answer)

# 2nd
import sys
input = sys.stdin.readline

N = int(input())
lst = []

for _ in range(N):
    lst.append(list(map(int, input().split())))

lst.sort()

dp = [1] * N
for i in range(N):
    for j in range(i):
        if lst[i][1] > lst[j][1] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
print(N - max(dp))