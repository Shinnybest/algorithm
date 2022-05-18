# bisect_left => 그 자리 인덱스
# bisect_right =>  그 다음자리 인덱스

import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
lst = [A[0]]
for i in range(1, N):
    if lst[-1] < A[i]:
        lst.append(A[i])
    else:
        idx = bisect_left(lst, A[i])
        lst[idx] = A[i]
print(len(lst))