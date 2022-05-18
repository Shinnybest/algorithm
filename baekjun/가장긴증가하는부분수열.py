import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

length = [1] * N
for i in range(N):
    for j in range(i):
        if A[j] < A[i]:
            length[i] = max(length[i], length[j] + 1)
print(max(length))