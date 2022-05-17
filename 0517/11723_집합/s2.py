import sys
sys.stdin = open('input.txt')

m = int(sys.stdin.readline())
my_set = set()

for i in range(m):
    op = sys.stdin.readline().strip()
    if not op[:3] == 'all' and not op[:5] == 'empty':
        op, num = op.split()
    num = int(num)
    if op == 'add':
        my_set.add(num)
    elif op == 'check':
        if num in my_set:
            print(1)
        else:
            print(0)
    elif op == 'remove':
        my_set.discard(num)
    elif op == 'toggle':
        if num in my_set:
            my_set.discard(num)
        else:
            my_set.add(num)
    elif op == 'all':
        my_set = set([i for i in range(1, 21)])
    elif op == 'empty':
        my_set = set()
