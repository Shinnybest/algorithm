import sys

N = int(input())
stack = []

for i in range(N):
    command = sys.stdin.readline().split()
    order = command[0]

    if order == 'push':
        value = command[1]
        stack.append(value)

    elif order == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())

    elif order == 'size':
        print(len(stack))

    elif order == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])


    elif order == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)