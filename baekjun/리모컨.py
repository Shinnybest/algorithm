N = int(input())  # 채널번호
M = int(input())  # 고장난 버튼의 개수
remote = {str(x) for x in range(10)}  # 총 리모컨 버튼 숫자

if M != 0:
    remote -= set(input().split())  # 고장난 버튼은 제외

min_cnt = abs(100-N)  # 일단 100과의 갭을 최소로 두고 계산

for k in range(1000000):
    num = str(k)
    for i in range(len(num)):
        if num[i] not in remote:  # 0~999999까지의 숫자 돌면서 가능한 리모컨 버튼 X -> pass
            break
        if i == len(num)-1:  # 마지막 자리수까지 확인 후 min_cnt 갱신
            min_cnt = min(min_cnt, abs(N-k)+len(num))

print(min_cnt)