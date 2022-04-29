import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
schedule = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [0] * (N+1)

total = 0
for i in range(N):
    total = max(total, dp[i])
    if i+schedule[i][0] > N:
        continue
    dp[i+schedule[i][0]] = max(total+schedule[i][1], dp[i+schedule[i][0]])

print(max(dp))

