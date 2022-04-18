import sys
sys.stdin = open('input.txt')

N = int(input())

p_arr = []
for _ in range(N):
    p_arr.append(tuple(map(int, input().split())))


for i in range(N):
    rank = 1
    for j in range(N):
        if p_arr[i][0] < p_arr[j][0] and p_arr[i][1] < p_arr[j][1]:
            rank += 1
    print(rank, end=" ")