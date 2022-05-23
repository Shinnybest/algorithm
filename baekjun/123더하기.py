# 1st. 30840 KB, 68ms
N = int(input())
lst = []
for _ in range(N):
    lst.append(int(input()))

def recurring(current, so_far):
    for i in range(1, 4):
        if current - i > 0:
            new_current = current - i
            so_far.append(i)
            recurring(new_current, so_far)
        elif current - i == 0:
            so_far.append(i)
            global answer_list
            answer_list.append(so_far)
        else:
            return

for i in range(N):
    answer_list = []
    recurring(lst[i], [])
    print(len(answer_list))