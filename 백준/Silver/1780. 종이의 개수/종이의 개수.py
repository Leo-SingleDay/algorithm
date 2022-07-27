import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def check(i, j, d):
    global paper
    pick = table[i][j]
    for it in range(i, i+d):
        for jt in range(j, j+d):
            if pick != table[it][jt]:
                newd = d//3
                for mi in range(0, 3):
                    for mj in range(0, 3):
                        check(i + mi*newd, j + mj*newd, newd)
                return

    paper[pick] += 1

n = int(input())
table = [list(map(int, input().split())) for _ in range(n)]
paper = [0, 0, 0]   # 0의 갯수, 1의 갯수, -1의 갯수
check(0, 0, n)
for i in range(-1, 2):
    print(paper[i])
