import sys
sys.stdin = open('input.txt')

M = int(input())
N = int(input())

total = 0
min_num = -1
flag = 1
for num in range(M, N+1):
    if num > 1:
        for i in range(2, num):
            if not num % i:
                break
        else:
            total += num
            if flag:
                min_num = num
                flag = 0
if not flag:
    print(total)
print(min_num)
