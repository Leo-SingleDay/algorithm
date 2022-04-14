import sys
sys.stdin = open('input.txt')

for _ in range(1, int(input())+1):
    n = int(input())
    cnt = 0
    to_bin = []
    while n > 0:
        if n % 2 == 1:
            to_bin.append(str(cnt))
        cnt += 1
        n = n//2
    print(' '.join(to_bin))


