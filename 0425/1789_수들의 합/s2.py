import sys
sys.stdin = open('input.txt')

def dfs(x,y):
    global cnt
    if x < 0 or x >= N or y < 0 or y >= N:
        return False

    if field[x][y] == 1:
        cnt += 1
        field[x][y] = 0
        for arrow in range(4):
            dfs(x+dx[arrow], y+dy[arrow])
        return True

# 상 하 좌 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

N = int(input())
field = [list(map(int, input())) for _ in range(N)]
villages = []
cnt = 0

for i in range(N):
    for j in range(N):
        if dfs(i, j):
            villages.append(cnt)
            cnt = 0

print(len(villages))
villages.sort()
for village in villages:
    print(village)