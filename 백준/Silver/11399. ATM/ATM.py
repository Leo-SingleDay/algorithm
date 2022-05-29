import sys

n = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))

p.sort()
sum = 0
cnt = 0
for i in p:
    cnt += i
    sum += cnt
print(sum)