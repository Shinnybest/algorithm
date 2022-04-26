def solution(s):
    total_length = len(s)
    divisor = []
    for i in range(1, total_length+1):
        if total_length % i == 0:
            divisor.append(i)

    print("divisor ", divisor)
    
    answer_list = []

    for num in divisor:
        tmp = s[0:num]
        cnt = 1
        multiple_num = total_length // num
        new = ''
        prev = ''

        for i in range(1, multiple_num):
            if tmp == s[num*i:num*(i+1)]:
                cnt += 1
                new = str(cnt) + tmp
                print("new ", new)
            else:
                prev += new
                prev += tmp
                tmp = s[num*i:num*(i+1)]
                cnt = 1
                new = ''
                print("prev ", prev)
        answer_list.append(len(prev))

    answer = min(answer_list)
    print(answer)
    return answer

solution("abcabcabcabcdededededede")