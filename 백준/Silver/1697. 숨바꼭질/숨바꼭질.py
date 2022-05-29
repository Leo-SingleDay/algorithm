import sys
from collections import deque

def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            print(visited[x])
            break
        for nx in (x+1, x-1, x*2):
            if 0 <= nx <= maxdot and not visited[nx]:
                visited[nx] = visited[x] + 1
                q.append(nx)

maxdot = 10 ** 5
visited = [0] * (maxdot+1)

n, k = map(int, sys.stdin.readline().split())
bfs()