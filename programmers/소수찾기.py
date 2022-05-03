# 복습
# permutations
# 소수
# str을 list로 하나씩 뽑아내는 방법
# join 사용법
from array import array
from itertools import permutations

def is_prime_number(number):
    if number < 2:
        return False
    else:
        for i in range(2, number):
            if number % i == 0:
                return False
        return True

def solution(numbers):
    numbers = list(numbers) # str을 list로 하나씩 뽑아내는 방법
    p = []
    array = []
    array2 = []
    for i in range(1, len(numbers) + 1):
        temp = permutations(numbers, i)
        for i in temp:
            temp_str = "".join(i)
            array.append(int(temp_str))

    print(array)
    print(len(array))
    for i in range(len(array)):
        print(i)
        if is_prime_number(array[i]):
            array2.append(array[i])
        
    array2 = set(array2)

    print(array2)

    return len(set(array2))

solution("011")