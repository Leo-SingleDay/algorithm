import sys
sys.stdin = open('input.txt')

N = int(input())

p_arr = []
result = []
for i in range(N):
    p_arr.append(list(map(int,input().split())))

