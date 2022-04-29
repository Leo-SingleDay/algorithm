import sys
sys.stdin = open('input.txt')

n = int(sys.stdin.readline())

t, p = [], []
dp = [0] * (n+1)
for _ in range(n):
    a,b = map(int, sys.stdin.readline().split())
    t.append(a)
    p.append(b)

total = 0
for i in range(n):
    count = max(dp[i], total)
    if i+t[i] > n:
        continue
    dp[i+t[i]] = max(dp[i+t[i]], count+p[i])
print(max(dp))



