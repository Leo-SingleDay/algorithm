import sys
sys.stdin = open('input.txt')

def check(field):
    max_cnt = 1
    for i in range(N):
        # 가로
        cnt = 1
        for j in range(1, N):
            if field[i][j] == field[i][j-1]:
                cnt += 1
            else:
                cnt = 1
            if cnt > max_cnt:
                max_cnt = cnt

        # 세로
        cnt = 1
        for k in range(1, N):
            if field[k][i] == field[k-1][i]:
                cnt += 1
            else:
                cnt = 1
            if cnt > max_cnt:
                max_cnt = cnt

    return max_cnt

N = int(input())
field = [list(input()) for _ in range(N)]
ans = 0

for i in range(N):
    for j in range(N):
        if j+1 < N:
            field[i][j], field[i][j+1] = field[i][j+1], field[i][j]
            count = check(field)
            if count >= ans:
                ans = count
            field[i][j], field[i][j + 1] = field[i][j + 1], field[i][j]

        if i+1 < N:
            field[i][j], field[i + 1][j] = field[i + 1][j], field[i][j]
            count = check(field)
            if count >= ans:
                ans = count
            field[i][j], field[i + 1][j] = field[i + 1][j], field[i][j]
    if ans == N:
        print(ans)
        exit()
print(ans)










