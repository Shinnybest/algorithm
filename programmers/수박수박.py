# 1st
def solution(n):
    num = n//2
    if n%2==0:
        return "수박" * num    
    else:
        return "수박" * num + "수"

# 다른 사람의 풀이
def water_melon(n):
    s = "수박" * n
    return s[:n]