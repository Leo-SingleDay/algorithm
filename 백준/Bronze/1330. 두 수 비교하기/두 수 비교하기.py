import sys
a,b = map(int, sys.stdin.readline().split())
ope = ''

if a>b:
    ope='>'
elif a<b:
    ope='<'
else:
    ope='=='
print(ope)