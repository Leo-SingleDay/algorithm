import sys
sys.stdin = open('input.txt')

n = int(sys.stdin.readline())

nums = [int(sys.stdin.readline().strip()) for _ in range(n)]

nums.sort()

for num in nums:
    print(num)