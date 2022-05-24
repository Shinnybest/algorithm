def solution(s):
    # s = (s[1:-1] + ",").split("},")[:-1]

    s = s.lstrip('{').rstrip('}').split('},{')
    print(s)

    dict = {}
    for i in range(len(s)):
        # split_nums = s[i][1:].split(",")
        split_nums = s[i].split(",")
        dict[len(split_nums)] = split_nums
    
    prev = []
    answer = []
    
    for i in range(1, len(s)+1):
        for num in dict[i]:
            if num not in prev:
                answer.append(int(num))
                break
        prev = dict[i]
    return answer

solution("{{20,111},{111}}")