N, M = map(int, input().split())
list = []
for _ in range(N):
    list.append(int(input()))

for i in range(N):
    if list[i] > M:
        list = list[:i]
        break

cnt = 0
while M > 0:
    for i in range(len(list), 0, -1):
        cnt += M // list[i]
        M = M - cnt * list[i]

print(cnt)