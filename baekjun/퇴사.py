# 1st 68ms 30840KB
import sys

N = int(sys.stdin.readline())
days = [[0,0]]
for _ in range(N):
    days.append(list(map(int, sys.stdin.readline().strip().split())))

answer = 0
for i in range(len(days)):
    if i + days[i][0] > len(days):
        days[i][1] = 0

def solution(day, income):
    global answer
    answer = max(answer, income)
    if day > len(days)-1:
        return
    for i in range(0, days[day][0]):
        if day + i > len(days)-1:
            break
        n_day = days[day + i][0] + day + i
        n_income = income + days[day + i][1]
        solution(n_day, n_income)
solution(1, 0)
print(answer)