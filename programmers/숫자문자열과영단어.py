def solution(s):
    num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    num_eng = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        
    answer = ""
    temp = ""
    
    for i in range(len(s)):
        if s[i] in num:
            answer += s[i]
        else:
            temp = temp + s[i]
            if temp in num_eng:
                answer += str(num_eng.index(temp))
                temp = ""
    
    return int(answer)

# 다른 사람의 풀이
def solution_1(s):
    num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)

def solution_2(s):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i in range(len(words)):
        s = s.replace(words[i], str(i))

    return int(s)