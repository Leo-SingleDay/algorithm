import sys
sys.stdin = open('input.txt')

N = int(input())
num_arr = list(map(int, input().split()))

answer = 0

for num in num_arr:
    if num == 1:
        pass
    else:
        for j in range(2 ,num):
            if(num/j == num//j):
                break
        else:
            answer += 1
print(answer)


