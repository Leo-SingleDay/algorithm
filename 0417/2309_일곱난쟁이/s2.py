import sys
sys.stdin = open('input.txt')

def find_dwarf(depth, start):
    if depth == 7:
        if sum(selected_dwarf) == 100:
            print('\n'.join(map(str, sorted(selected_dwarf))))
            exit()
        else:
            return

    for i in range(start, len(dwarf_list)):
        selected_dwarf.append(dwarf_list[i])
        find_dwarf(depth+1, i + 1)
        selected_dwarf.pop()

dwarf_list = [int(input()) for _ in range(9)]
selected_dwarf = []

find_dwarf(0, 0)
