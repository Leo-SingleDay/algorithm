import sys
sys.stdin = open('input.txt')

def find_minmax(count, total):
    global max_num, min_num

    if count == len(nums):
        if total > max_num:
            max_num = total
        if total < min_num:
            min_num = total
        return

    for j in range(4):
        if ops[j] > 0:
            ops[j] -= 1
            if j == 0:
                find_minmax(count+1, total+nums[count])
            if j == 1:
                find_minmax(count+1, total-nums[count])
            if j == 2:
                find_minmax(count+1, total*nums[count])
            if j == 3:
                find_minmax(count+1, int(total/nums[count]))
            ops[j] += 1


N = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))

max_num = -1e9
min_num = 1e9

find_minmax(1, nums[0])
print(max_num)
print(min_num)

