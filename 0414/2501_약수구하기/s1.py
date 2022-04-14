import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())

count = 0
divisor = 1
while divisor < N:
    if N % divisor == 0:
        count += 1

    if count == K:
        break

    divisor += 1

if count < K:
    print(0)
else:
    print(divisor)