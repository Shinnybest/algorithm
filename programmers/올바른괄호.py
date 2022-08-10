def solution(s):
    left = '('
    right = ')'
    lst = []
    for i in range(len(s)):
        if s[i] == left:
            lst.append(left)
        elif s[i] == right and len(lst) > 0:
            lst.pop()
        elif s[i] == right and len(lst) == 0:
            return False
    if len(lst) == 0:
        return True
    else:
        return False