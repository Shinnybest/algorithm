M = int(input())

graph = [['*' for j in range(M)] for i in range(M)]

def empty(size, x, y):
    for i in range(x+size//3, x+2*size//3):
        for j in range(y+size//3, y+2*size//3):
            graph[i][j]=" "

size = 3
while size<=M:
    for i in range(0, M, size):
        for j in range(0, M, size):
            empty(size, i, j)
    size = size*3

for i in range(M):
    str = ''.join(graph[i])
    print(str)