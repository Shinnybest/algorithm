import heapq

N = int(input())
left = []
right = []
answers = []

for _ in range(N):
    num = int(input())
    
    if len(left) == len(right):
        heapq.heappush(left, (-num, num))
    else:
        heapq.heappush(right, (num, num))
    
    if right and left[0][1] > right[0][1]:
        l = heapq.heappop(left)[1]
        r = heapq.heappop(right)[1]
        heapq.heappush(right, (-l, l))
        heapq.heappush(left, (-r, r))
    answers.append(left[0][1])

for answer in answers:
    print(answer)