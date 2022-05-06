import sys
from collections import deque
sys.stdin = open('input.txt')

n = int(sys.stdin.readline())

nums = [int(sys.stdin.readline()) for _ in range(n)]

stack = deque()
result = []
i = 1
for num in nums:
    while i <= num:
        stack.append(i)
        result.append('+')
        i += 1

    if stack[len(stack)-1] == num:
        stack.pop()
        result.append('-')
    else:
        print('NO')
        exit()
print('\n'.join(result))
