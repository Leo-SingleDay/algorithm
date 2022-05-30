def dfsStack(v, g):
    stack = [v]
    while stack:
        cur = stack.pop()
        for node in g[cur]:
            if visited[node] == 0:
                stack.append(node)
        visited[cur] = 1

n = int(input()) #노드의 갯수
e = int(input()) #간선의 갯수
g = [[] for _ in range(n + 1)] #연결리스트
visited = [0] * (n + 1)

for _ in range(e):
    v, w = map(int, input().split())
    g[v].append(w)
    g[w].append(v)


dfsStack(1, g)
print(visited.count(1) - 1)