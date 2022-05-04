from collections import deque

def solution(N, cnt, numbers):
    list = [i for i in range(1, N)]
    queue = deque(list)
    result = []
    for i in range(0, cnt):
        cnt = 0
        current = queue.index(numbers[i])
        # if current < len(numbers) - current:
        print(current)
        print(queue)
        if current == 0:
            f_element = queue.popleft()
            queue.append(f_element)
            cnt = 0
        else:
            while current > 0:
                current -= 1
                f_element = queue.popleft()
                queue.append(f_element)
                cnt += 1
        result.append(cnt)
        # else:
    print(sum(result))
    return result

solution(10, 3, [2, 9, 5])








