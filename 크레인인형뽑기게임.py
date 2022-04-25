from collections import defaultdict

def solution(board, moves):
    dict = defaultdict(list)
    basket = []
    answer = 0
    for i in range(len(board)):
        for m in range(len(board)):
            if board[i][m] == 0:
                continue
            dict[m+1] += [board[i][m]]
    
    for i in range(len(moves)):
        if len(dict[moves[i]]) != 0:
            basket.append(dict[moves[i]][0])
            dict[moves[i]].pop(0)
            if i > 0 and len(basket) >= 2 and basket[-1] == basket[-2]:
                basket.pop()
                answer += 1
                basket.pop()
                answer += 1          
    return answer

# 다른 사람의 풀이
def solution_1(board, moves):
    stacklist = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stacklist.append(board[j][i-1])
                board[j][i-1] = 0

                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2     
                break
    return answer