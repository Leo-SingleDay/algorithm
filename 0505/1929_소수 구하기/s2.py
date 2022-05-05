import sys
sys.stdin = open('input.txt')

m, n = map(int, sys.stdin.readline().split())
n += 1
sieve = [True] * n
l = int(n ** 0.5)
for i in range(2, l+1):
    if sieve[i]:
        for j in range(i+i, n, i):
            sieve[j] = False

for k in range(m, n):
    if k > 1 and sieve[k]:
        print(k)

