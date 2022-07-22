import sys

n, m = map(int, sys.stdin.readline().split())

nums = [0] + list(map(int, sys.stdin.readline().split()))
dp = [0]

for i in range(1, n+1):
    next_num = dp[i-1] + nums[i]
    dp.append(next_num)

for j in range(m):
    n1, n2 = map(int, sys.stdin.readline().strip().split())
    print(dp[n2]-dp[n1-1])