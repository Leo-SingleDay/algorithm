import sys
sys.stdin = open('input.txt')

from itertools import combinations
import itertools

dwarf_list = [int(input()) for _ in range(9)]

c = list(combinations(dwarf_list, 7))
for i in c:
    if sum(i) == 100:
        print('\n'.join(map(str, sorted(i))))
        break

