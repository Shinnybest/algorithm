N, M = map(int, input().split())
lst = list(map(int, input().split()))

start, end = 0, max(lst)

while start <= end:
    mid = (start + end) // 2
    timber = 0
    for i in range(N):
        if lst[i] > mid:
            timber += (lst[i] - mid)
    # 최소 M 길이의 목재를 얻기 위한 최대값을 찾아야 하니까 timber = M일 경우
    # start를 더 큰쪽 (오른)으로 옮기고 안 되면 end를 답으로 하는게 맞다.
    if timber >= M:
        start = mid+1
    else:
        end = mid-1

print(end)