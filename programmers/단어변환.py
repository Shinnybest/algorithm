# def check(begin, target, words, cnt):
#         print("begin : ", begin, "target : ", target, "words : ", words)
#         if begin == target:
#             print("target", target)
#             answer.append(cnt)
#             return
            
#         for word in words:
#             if word[0] + word[1] == begin[0] + begin[1]:
#                 cnt += 1
#                 words.remove(word)
#                 return check(word, target, words, cnt)
#             if word[0] + word[2] == begin[0] + begin[2]:
#                 cnt += 1
#                 words.remove(word)
#                 return check(word, target, words, cnt)
#             if word[1] + word[2] == begin[1] + begin[2]:
#                 cnt += 1
#                 words.remove(word)
#                 return check(word, target, words, cnt)
#         return
# def solution(begin, target, words):
    
#     global answer
#     answer = []    
#     cnt = 0
#     if target in words:
#         check(begin, target, words, cnt)
#     else:
#         return 0
    
#     return min(answer)

# solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])

# https://programmers.co.kr/learn/courses/30/lessons/43163
# 성공 풀이
global answer
def dfs(begin, target, words, visit):
    answer = 0
    stacks = [begin]
    while stacks:
        stack = stacks.pop()
        if stack == target:
            return answer
        
        for i in range(len(words)):
            if len([j for j in range(len(words[i])) if words[i][j] != stack[j]]) == 1:
                
                if visit[i] != 0:
                    continue
                visit[i] = 1
                stacks.append(words[i])
        answer += 1
    return answer

def solution_1(begin, target, words):
    if target not in words:
        return 0
    visit = [0 for i in words]
    answer = dfs(begin, target, words, visit)
    print(answer)
    return answer

solution_1("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])