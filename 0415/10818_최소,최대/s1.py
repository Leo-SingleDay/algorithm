import sys
sys.stdin = open('input.txt')

N = int(input())
nums = list(map(int,input().split()))

min_num = nums[0]
max_num = nums[0]

for i in range(1, len(nums)):
    if nums[i] < min_num:
        min_num = nums[i]
    if nums[i] > max_num:
        max_num = nums[i]
print(min_num, end=" ")
print(max_num)
