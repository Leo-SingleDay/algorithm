from sys import stdin, stdout

_ = stdin.readline()
A = set(stdin.readline().split())
_ = stdin.readline()
M_nums = stdin.readline().split()

for num in M_nums:
    if num in A:
        stdout.write('1\n')
    else:
        stdout.write('0\n')
