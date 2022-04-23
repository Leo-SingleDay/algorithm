import sys
sys.stdin = open('input.txt')

n, k = list(map(int, input().split()))

dp = [0 for _ in range(k+1)]
dp[0] = 1
coins = []

for _ in range(n):
    coins.append(int(input()))

for coin in coins:
    for i in range(1, k+1):
        if i-coin >= 0:
            dp[i] += dp[i-coin]

print(dp[k])
