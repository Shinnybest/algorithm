# number = int(input())

# def check(number):
#     stack = [0, 0]
#     if number < 10:
#         stack[0] = 0
#         stack[1] = number
#         return stack[1] * 10 + stack[1]
#     else:
#         stack[0] = number // 10
#         stack[1] = number - stack[0] * 10
#         return stack[1] * 10 + (stack[0] + stack[1]) % 10

# new_number = check(number)
# cycle_length = 0
# while number != new_number:
#     check(new_number)
#     cycle_length += 1
    
# print(cycle_length)

n = int(input())
num=n
cnt = 0

while True:
    a = num // 10
    b = num % 10
    c = (a+b) % 10
    num = b*10+c
    cnt = cnt + 1
    if n == num:
        break

print(cnt)