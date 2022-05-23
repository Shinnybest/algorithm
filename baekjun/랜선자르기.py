# 1-passed
import sys

N, M = map(int, input().split())
lst = []
for _ in range(N):
    lst.append(int(sys.stdin.readline()))

start, end = 0, max(lst) # 최소 값 start를 0으로 해주면 아래 zero division error 나지 않게 조건문이 필요하다!

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for tree in lst:
        if mid == 0:
            cnt = sum(lst)
            break
        if tree>=mid:
            cnt += (tree // mid)
    if cnt >= M:
        start = mid+1
    else:
        end = mid - 1

print(end)

# 2-passed
import sys

N, M = map(int, input().split())
lst = []
for _ in range(N):
    lst.append(int(sys.stdin.readline()))

start, end = 1, max(lst) # 최소 값 start를 1로 해준다.

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for tree in lst:
        if tree>=mid:
            cnt += (tree // mid)
    if cnt >= M:
        start = mid+1
    else:
        end = mid - 1

print(end)