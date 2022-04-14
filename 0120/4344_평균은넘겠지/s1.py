import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    tmp = list(map(int,input().split()))
    avg_num = (sum(tmp) - tmp[0])/tmp[0]
    gt_avg = 0
    for i in range(1, tmp[0]+1):
        if tmp[i] > avg_num:
            gt_avg += 1
    result = round(gt_avg / tmp[0] * 100, 3)
    score = '{:.3f}'.format(result)
    print(score, end='%')
    print()
