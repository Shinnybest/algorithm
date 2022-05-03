n = int(input())
count = 0
stack = []
result = []
no_message = False

while count < n:
    x = int(input())
    while count < x:
        count += 1
        stack.append(count)
        result.append("+")
    if stack[-1] == x:
        stack.pop()
        result.append("-")
    else:
        no_message = True
        exit(0)

if no_message == True:
    print("NO")
else:
    print("\n".join(result))