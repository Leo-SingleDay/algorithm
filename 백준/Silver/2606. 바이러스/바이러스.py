import sys

def dfsStack(v, edges):
    stack = [v]
    while stack:
        cur = stack.pop()
        for node in edges[cur]:
            if visited[node] == 0:
                stack.append(node)
        visited[cur] = 1


c = int(sys.stdin.readline())
e = int(sys.stdin.readline())
edges = [[] for _ in range(c+1)]
visited = [0] * (c+1)
for _ in range(e):
    e1, e2 = map(int, sys.stdin.readline().split())
    edges[e1].append(e2)
    edges[e2].append(e1)

dfsStack(1, edges)
print(visited.count(1) - 1)