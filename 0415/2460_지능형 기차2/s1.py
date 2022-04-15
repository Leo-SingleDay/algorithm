import sys
sys.stdin = open('input.txt')

p_count = 0
max_count = 0
for st_num in range(1, 11):
    p_out, p_in = map(int, input().split())
    p_count -= p_out
    p_count += p_in
    if p_count > max_count:
        max_count = p_count
print(max_count)


