import sys
sys.stdin = open('input.txt')

a, b = list(map(int, input().split()))

num_list = []
for i in range(1, 46):
    num_list += [i] * i

print(sum(num_list[a-1:b]))