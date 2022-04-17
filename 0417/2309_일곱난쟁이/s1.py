import sys
sys.stdin = open('input.txt')

def find_dwarfs():
    for i in range(len(dwarf_list)-1):
        for j in range(i+1, 9):
            if sum_height - (dwarf_list[i] + dwarf_list[j]) == 100:
                dwarf1, dwarf2 = dwarf_list[i], dwarf_list[j]
                dwarf_list.remove(dwarf1)
                dwarf_list.remove(dwarf2)
                break

        if len(dwarf_list) == 7:
            print('\n'.join(map(str, sorted(dwarf_list))))
            return


dwarf_list = [int(input()) for i in range(9)]
sum_height = sum(dwarf_list)

find_dwarfs()

