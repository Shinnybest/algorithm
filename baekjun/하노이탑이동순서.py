# def solution(N):
#     answer = 0
#     stack_1 = [0] + [i for i in range(N, 0, -1)]
#     stack_2 = [0]
#     print(stack_1)
#     cnt = N
#     answer_list = []
#     def dfs(cnt, stack_1, stack_2, move_list):
#         if cnt == 0:
#             return move_list
#         stack_3 = [0]
#         while stack_3[-1] != cnt:
#             if stack_1[-1] < stack_2[-1] or stack_2[-1] == 0:
#                 ele = stack_1.pop()
#                 stack_2.append(ele)
#             elif 
#         dfs(cnt-1, stack_1, stack_2)    
#     lst = dfs(cnt, stack_1, stack_2, answer_list)
#     print(len(lst))
#     return lst
# solution(3)

def hanoi(N, a, b, c):
    if N == 1:
        move_list.append([a, c])
    else:
        hanoi(N-1, a, c, b)
        move_list.append([a, c])
        hanoi(N-1, b, a, c)

move_list = []
hanoi(int(input()), 1, 2, 3)