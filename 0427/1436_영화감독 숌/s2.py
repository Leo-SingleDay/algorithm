import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline().strip())

ans = 0
ans_num = 0
for i in range(666, 999999999999):
    if ans == N:
        break

    for j in range(len(str(i))-2):
        if str(i)[j] == '6' and str(i)[j] == str(i)[j+1] == str(i)[j+2]:
            ans += 1
            ans_num = i
            break

print(ans_num)