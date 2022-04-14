import sys
sys.stdin = open("input.txt")

N = int(input())
nums = list(map(int, input().split()))

min_num = 1000000
max_num = -1000000

for i in range(N):
    if nums[i] <= min_num:
        min_num = nums[i]
    if nums[i] >= max_num:
        max_num = nums[i]

print(min_num, max_num)
