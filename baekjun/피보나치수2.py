M = int(input())
nums = [i for i in range(M+1)]

for i in range(2, M+1):
    nums[i] = nums[i-1] + nums[i-2]

print(nums[-1])