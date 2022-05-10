import sys
sys.setrecursionlimit(10000)
sys.stdin = open('input.txt')

dx = [0, 0, -1, 1] # 상 하 좌 우
dy = [-1, 1, 0, 0]

def dfs(x, y, flag):
    global count
    if field[x][y] and flag:
        count += 1
        flag = False
    field[x][y] = 0
    for arrow in range(4):
        nx = x + dx[arrow]
        ny = y + dy[arrow]
        if 0 <= nx < m and 0 <= ny < n:
            if field[nx][ny]:
                dfs(nx, ny, flag)


for _ in range(int(sys.stdin.readline())):
    m, n, k = map(int, sys.stdin.readline().split())
    field = [[0] * n for _ in range(m)]
    targets = []
    count = 0
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        targets.append((x, y))
        field[x][y] = 1
    for tx, ty in targets:
        if field[tx][ty]:
            dfs(tx, ty, True)
    print(count)



