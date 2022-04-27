import sys
sys.stdin = open('input.txt')

while True:
    nums = str(sys.stdin.readline().strip())
    if nums == '0':
        break
    for i in range(len(nums)//2):
        if nums[i] != nums[-1-i]:
            print('no')
            break
    else:
        print('yes')

