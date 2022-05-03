def check(n):
    cnt = 0
    while n > 0:
        if n % 2 == 0:
            n = n / 2
        else:
            n = n - 1
            cnt += 1
    return cnt

def solution(n):
    return check(n)


def solution_1(n):
    cnt = 0
    while n>0:
        q, r = divmod(n, 2)
        n = q
        if r != 0:
            cnt += 1
    return cnt

# 이것만 통과!
def solution_2(N):
    answer = 0
    while N > 0:
        answer += N % 2
        N //= 2
    return answer

def solution_3(n):
    return bin(n).count('1')