import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    answer = input()
    tmp = 0
    result = 0
    for i in range(len(answer)):
        if answer[i] == 'O':
            tmp += 1
        else:
            tmp = 0
        result += tmp
    print(result)
