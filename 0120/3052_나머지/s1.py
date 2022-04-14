import sys
sys.stdin = open('input.txt')

arr = []
for tc in range(10):
    num = int(input()) % 42
    arr.append(num)

arr = set(arr)

print(len(arr))

