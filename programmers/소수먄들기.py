from itertools import combinations

def is_prime(num):
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def solution(nums):
    sum_arr = []
    is_prime_number = []
    temp = combinations(nums, 3)
    for i in temp:
        sum_num = sum(i)
        sum_arr.append(sum_num)
        
    for i in sum_arr:
        if is_prime(i):
            is_prime_number.append(i)
    
    return len(is_prime_number)