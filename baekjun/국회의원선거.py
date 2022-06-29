import heapq

N = int(input())
heap = []
dasom = int(input())
for _ in range(N-1):
    heapq.heappush(heap, -int(input()))

cnt = 0
if heap:
    vote = heapq.heappop(heap)
    while -vote >= dasom:
        cnt += 1
        n = -vote - 1
        heapq.heappush(heap, -n)
        dasom += 1
        vote = heapq.heappop(heap)

print(cnt)