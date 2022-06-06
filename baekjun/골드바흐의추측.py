N = int(input())

array = [True for i in range(1000001)]

# '에라토스테네스의 체'를 알아야 시간초과에서 벗어날 수 있다.
for i in range(2, 1001):
    if array[i]:
        for k in range(i + i, 1000001, i):
            array[k] = False

while N >=6:
    for i in range(3, len(array)):
        if array[i] and array[N-i]:
            print(N, '=', i, '+', N-i)
            break
    N = int(input())