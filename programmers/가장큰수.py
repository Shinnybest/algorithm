def solution(numbers):
    numbers = list(map(str, numbers))
    # 기본은 오름차순이라 내림차순으로 바꾸기위해 reverse=True
    # x*3는 값 비교위해서
    numbers.sort(key = lambda x: x*3, reverse=True)
    # 000을 처리해주기 위해서 int로 바꾼 다음에 다시 str으로 변경
    answer = str(int(''.join(numbers)))    
    return answer