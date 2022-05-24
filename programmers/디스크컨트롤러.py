import heapq

def solution(jobs):
    answer, now, i = 0,0,0
    start = -1
    heap = []
    while i<len(jobs):
        for j in jobs:
            if start < j[0] <=now:
                heapq.heappush(heap, [j[1], j[0]])
        if len(heap) > 0:
            current = heapq.heappop(heap)
            start = now
            now = now + current[0]
            answer = answer + (now-current[1])
            i += 1
        else:
            now += 1
    return int(answer//len(jobs))


def solution2(jobs):
    tasks = sorted([(x[1], x[0]) for x in jobs], key=lambda x: (x[1], x[0]), reverse=True)
    q = []
    heapq.heappush(q, tasks.pop())
    current_time, total_response_time = 0, 0
    while len(q) > 0:
        dur, arr = heapq.heappop(q)
        current_time = max(current_time + dur, arr + dur)
        total_response_time += current_time - arr
        while len(tasks) > 0 and tasks[-1][1] <= current_time:
            heapq.heappush(q, tasks.pop())
        if len(tasks) > 0 and len(q) == 0:
            heapq.heappush(q, tasks.pop())
    return total_response_time // len(jobs)


solution2([[0, 3], [1, 9], [2, 6]])