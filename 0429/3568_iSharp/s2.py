import sys
sys.stdin = open('input.txt')

def solve(s):
    for i in range(len(s)-2, -1, -1):
        if s[i] == ']':
            print('[]', end='')
        elif s[i] == '[':
            continue
        elif s[i] in '&*':
            print(s[i], end='')
        else:
            print(' ', end='')
            for j in range(0, i+1):
                print(s[j], end='')
            print(';')
            return

datatype, *variable = sys.stdin.readline().split()
for s in variable:
    print(datatype, end='')
    solve(s)