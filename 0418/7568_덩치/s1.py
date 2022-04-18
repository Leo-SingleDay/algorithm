import sys
sys.stdin = open('input.txt')

N = int(input())

p_arr = []
result = [1 for _ in range(N)]
for i in range(N):
    p_arr.append(tuple(map(int, input().split() + [i])))
p_arr.sort(reverse=True, key=lambda x : (x[0], x[1]))

rank = 1
count = 0
for j in range(N-1):
    if p_arr[j][1] > p_arr[j+1][1]:
        result[p_arr[j][2]] = rank
        rank += (count + 1)
    else:
        result[p_arr[j][2]] = rank
        count += 1

result[p_arr[N-1][2]] = rank

print(' '.join(map(str, result)))



