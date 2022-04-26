import sys
sys.stdin = open('input.txt')

def find(x, y):
    global count, ans
    w_Start = 0
    b_Start = 0
    for i in range(x, x+8):
        for j in range(y, y+8):
            if (i + j) % 2 == 0:
                if field[i][j] != 'W': w_Start += 1
                if field[i][j] != 'B': b_Start += 1
            else:
                if field[i][j] != 'B': w_Start += 1
                if field[i][j] != 'W': b_Start += 1
    ans.append(w_Start)
    ans.append(b_Start)


N, M = list(map(int, input().split()))
field = [list(input()) for _ in range(N)]
ans = []

for i in range(N-7):
    for j in range(M-7):
        find(i, j)
        count = 0

print(min(ans))
