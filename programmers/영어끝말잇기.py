from collections import defaultdict

def solution(n, words):
    words = [words[0][0]] + words
    dict=defaultdict(list)
    a = len(words) // n
    for i in range(a):
        for j in range(1, n+1):
            if (i*n + j) == len(words):
                return [0, 0]
            b = words[i*n + j]
            dict[j].append(b)
            if b in words[:i*n + j] or b[0] != words[i*n + j - 1][-1]:
                return [j, len(dict[j])]
    return [0, 0]


solution(2, ["hello", "one", "even", "never", "now", "world", "draw"])