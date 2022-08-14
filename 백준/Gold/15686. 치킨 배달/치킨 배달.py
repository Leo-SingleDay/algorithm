import sys
from itertools import combinations
n,m = map(int, sys.stdin.readline().split(" "))
c = []
for _ in range(n):
    c.append(list(map(int , sys.stdin.readline().split(" "))))
house = []
chick = []
for i in range(n):
    for t in range(n):
        if c[i][t] == 1:
            house.append([i,t])
        elif c[i][t] == 2:
            chick.append([i,t])

def way(x,y,x1,y1):
    return abs(x-x1) + abs(y-y1)

ans = float("inf")
for t in combinations(chick,m):
    ww = 0
    for p in house:
        chic_way = []
        for k in t:
            chic_way.append(way(k[0],k[1],p[0],p[1]))
        ww += min(chic_way)
    if ww < ans:
        ans = ww
print(ans)