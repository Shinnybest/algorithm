from sys import stdin
n = stdin.readline()
N = sorted(map(int,stdin.readline().split()))
m = stdin.readline()
M = map(int, stdin.readline().split())

answer = [0] * m
for i in range(m):
    target = M[i]
    start = 1
    end = n
    while start <= end:
        mid = (start + end) // 2
        if target < mid:
            end = mid-1
        elif target > mid:
            start = mid+1
        elif target == mid:
            answer[i] = 1
            break

for i in answer:
    print(i)