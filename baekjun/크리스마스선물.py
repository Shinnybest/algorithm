import heapq

N = int(input())
gift = []
for _ in range(N):
    a = list(map(int, input().split()))
    if a[0] == 0:
        if len(gift) == 0:
            print(-1)
        else:
            t = -heapq.heappop(gift)
            print(t)
    else:
        for i in range(a[0]):
            heapq.heappush(gift, -a[i+1])