def solution(sentence):
    dict = {")": "(", "]": "["}

    stack = []
    for i in range(len(sentence)):
        if sentence[i] == "(" or sentence[i] == "[":
            print(sentence[i])
            stack.append(sentence[i])
        elif sentence[i] == ")" or sentence[i] == "]":
            print(stack)
            print(sentence[i])
            if stack[-1] != dict[sentence[i]]:
                break
            else:
                stack.pop()
    if stack == []:
        print(stack)
        print("yes")

    else:
        print("no")

solution("Help( I[m being held prisoner in a fortune cookie factory)].")



