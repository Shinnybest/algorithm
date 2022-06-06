N, M = map(int, input().split())
co = []
for _ in range(N):
    co.append(int(input()))
co.sort()

start = 1
end = co[-1] - co[0]
answer = 0

while start <= end:
    mid = (start + end) // 2
    old = co[0]
    count = 1

    for i in range(1, N):
        if mid + old <= co[i]:
            old = co[i]
            count += 1
    if count < M:
        end = mid - 1
    else:
        start = mid + 1
        answer = mid
print(answer)