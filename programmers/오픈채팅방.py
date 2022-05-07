def solution(record):
    dict = {}
    result = []
    for i in record:
        words = i.split()
        if len(words) == 3:
            dict[words[1]] = words[2]

    for i in record:
        i = i.split()
        if i[0] == "Enter":
            result.append(dict[i[1]] + "님이 들어왔습니다.")
        elif i[0] == "Leave":
            result.append(dict[i[1]] + "님이 나갔습니다.")
    return result