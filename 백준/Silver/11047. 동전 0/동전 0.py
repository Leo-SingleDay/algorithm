import sys

n, k = map(int, sys.stdin.readline().split())

coins = []
result = 0

for i in range(n):
    coins.append(int(sys.stdin.readline()))

for l in range(len(coins)-1, -1, -1):
    if coins[l] > k:
        pass
    elif k == 0:
        pass
    else:
        divider = k // coins[l]
        result += divider
        k -= coins[l]*divider

print(result)
