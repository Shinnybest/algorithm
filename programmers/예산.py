import heapq


def solution(d, budget):
    d.sort()
    while sum(d)>budget:
        d.pop()
    return len(d)


arr = [1, 3, 2, 4, 2, 5, 7, 2]
heapq.heapify(arr)

print(arr)
# 힙으로는 안 된다. -> sort를 하면 오름차순 정렬이 되는데 heap으로 하게 되면 자식노드에서 형제끼리는 대소관계가 정렬이 안된다.