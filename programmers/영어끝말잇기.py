def solution(n, words):
    dict = {}
    for i in range(2, n+1):
        dict[i] = list()
    
    words_list = ["dummy"] + words
    for i in range(1, len(words)+1):
        if i%n == 0:
            dict[n] = words_list[i]
        else:
            print(i)
            dict[i%n] = words_list[i]
            
    answer = []
    
    for i in range(len(words_list)-1):
        if words_list[i] != words_list[i+1]:
            if (i+1) % n == 0:
                    print("해당내용", words_list[i+1])
                    index = dict[n].index(words_list[i+1])
                    answer.append[n, index]
            else:
                print(i+1)
                print("해당내용", words_list[i+3])
                print((i+1) % n)
                print(dict[(i+1) % n])
                print(dict[i+1])
                index = dict[(i+1) % n].index(words_list[i+3])
                answer.append[(i+1) % n, index]
                
        else:
            return [0, 0]
    
    already = []
    
    for i in range(len(words)):
        if words[i] in already:
            if (i) % n == 0:
                    index = dict[n].index()
                    answer.append[n, index]
    
            else:
                index = dict[(i) % n].index()
                answer.append[(i) % n, index]
        else:
            already.append(words[i])
    return answer

solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"])