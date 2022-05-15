import sys
sys.stdin = open('input.txt')

def factorial(n):
    if(n > 1):
        return n * factorial(n - 1)
    else:
        return 1

n = int(sys.stdin.readline())
fac_num = str(factorial(n))

cnt = 0
for i in range(len(fac_num)-1, -1, -1):
    if fac_num[i] == '0':
       cnt += 1
    else:
        break
print(cnt)