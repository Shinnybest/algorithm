import heapq

def solution(operations):
    heap = []
    max_heap = []
    for i in operations:
        sp = i.split(" ")
        if sp[0] == "I":
            n = int(sp[1])
            heapq.heappush(heap, n)
            heapq.heappush(max_heap, (n*(-1), n))
        else:
            if len(heap) == 0:
                continue
            if sp[1] == '-1':
                min_value = heapq.heappop(heap)
                max_heap.remove((min_value*-1, min_value))
            else:
                max_value = heapq.heappop(max_heap)[1]
                heap.remove(max_value)

    if heap:
        m = heapq.heappop(max_heap)[1]
        n = heapq.heappop(heap)
        return [m, n]
    else:
        return [0, 0]