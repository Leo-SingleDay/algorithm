import sys

def dfs(n):
    print(n, end= ' ')
    visited[n] = 1
    for i in nodes[n]:
        if not visited[i]:
            dfs(i)

def bfs(n):
    visited[n] = 1
    queue = [n]
    while queue:
        v = queue.pop(0)
        print(v, end=' ')
        for i in nodes[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1


N, M, V = map(int, sys.stdin.readline().split())
nodes = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(M):
    n1, n2 = map(int, sys.stdin.readline().split())
    nodes[n1].append(n2)
    nodes[n2].append(n1)

for i in range(1, N+1):
    nodes[i].sort()

dfs(V)
visited = [0 for _ in range(N+1)]
print()
bfs(V)

