import sys
sys.stdin = open('input.txt')

tmp = 1
result = [0 for _ in range(10)]

for i in range(3):
    tmp *= int(input())
tmp = str(tmp)

for j in range(len(tmp)):
    result[int(tmp[j])] = result[int(tmp[j])]+1

for k in range(10):
    print(result[k])


