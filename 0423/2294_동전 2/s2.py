import sys
sys.stdin = open('input.txt')

n, k = list(map(int, input().split()))

counts = [0 for _ in range(k+1)]

coins = []
for _ in range(n):
    coins.append(int(input()))

for i in range(1, k+1):
    temp = []
    for coin in coins:
        if i >= coin and counts[i-coin] != -1:
            temp.append(counts[i-coin])
    if not temp:

        counts[i] = -1
    else:
        counts[i] = min(temp) +1

print(counts[k])



