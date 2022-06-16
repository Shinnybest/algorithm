import itertools

lst = list(map(int, input().split()))

while lst[0] != 0:
    nCr = itertools.combinations(lst[1:], 6)
    for i in nCr:
        for j in i:
            print(j, end= " ") # 한칸 띄어쓰기
        print() # 줄 바꿈
    print() # 한줄 띄어쓰기
    lst = list(map(int, input().split()))