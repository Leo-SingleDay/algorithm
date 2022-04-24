import sys
sys.stdin = open('input.txt')

S = int(input())
for i in range(1, 4294967295):
    if i * (i+1) / 2 > S:
        print(i-1)
        break

