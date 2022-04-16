import sys
sys.stdin = open('input.txt')

def greatest_common(n1, n2):
    greatest_num = 1
    for i in range(1, min(n1, n2)+1):
        if n1 % i == 0 and n2 % i == 0:
            greatest_num = i
    return greatest_num


def least_common (n1, n2, gr):
    return int((gr * (n1/gr) * (n2/gr)))



n1, n2 = map(int,input().split())
gr = greatest_common(n1,n2)
le = least_common(n1, n2, gr)

print(gr)
print(le)
