import sys

n, m = map(int, sys.stdin.readline().split())
square = []
for _ in range(n):
    square.append(list(map(int, sys.stdin.readline().strip())))

check = min(n, m)
answer = 0
for i in range(n):
    for j in range(m):
        for k in range(check, -1, -1):
            if ((i + k) < n) and ((j+k) < m) and (square[i][j] == square[i][j+k] == square[i+k][j] == square[i+k][j+k]):
                answer = max(answer, (k+1) ** 2)
                break
print(answer)