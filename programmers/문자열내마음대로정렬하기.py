# 1st
def solution(strings, n):
    strings.sort()
    lst = []
    for i in strings:
        lst.append([i[n], i])    
    lst.sort(key = lambda x: x[0])
    answer = []
    for i in lst:
        answer.append(i[1])
    return answer

# 2nd
def solution(strings, n):
    strings.sort()
    return sorted(strings, key = lambda x:x[n])