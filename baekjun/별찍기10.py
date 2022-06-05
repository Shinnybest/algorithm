# M = int(input())
M = 27

graph = [['*' for j in range(M)] for i in range(M)]

def empty(size, i, j):
    return


size = 3
while size<=M:
    for i in range(0, M, size):
        for j in range(0, M, size):
            empty(size, i, j)

    size = size*3



for i in range(M):
    str = ''.join(graph[i])
    print(str)