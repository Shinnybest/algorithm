#1st solution
def dfs(so_far, new_num):
    lst = []
    for num in so_far:
        lst.append(num-new_num)
        lst.append(num+new_num)
    return lst

def solution(numbers, target):
    N = [0]
    for i in numbers:
        N = dfs(N, i)
    return N.count(target)

#2nd solution
def solution_2(numbers, target):
    answer = 0
    n = len(numbers)

    def dfs_2(idx, result):
        if idx == n:
            if result == target:
                nonlocal answer
                answer += 1
        else:
            dfs_2(idx + 1, result - numbers[idx])
            dfs_2(idx + 1, result + numbers[idx])
    dfs_2(0, 0)

    return answer