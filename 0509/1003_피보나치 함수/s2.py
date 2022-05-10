import sys
sys.stdin = open('input.txt')

for _ in range(int(sys.stdin.readline())):
    dp_zero = [1] + [0] * 40
    dp_one = [0] + [1] + [0] * 39
    n = int(sys.stdin.readline())
    if n == 0 or n == 1:
        print(dp_zero[n], dp_one[n])
        continue
    for i in range(2, n+1):
        dp_zero[i] = dp_zero[i-1] + dp_zero[i-2]
        dp_one[i] = dp_one[i-1] + dp_one[i-2]
    print(dp_zero[n], dp_one[n])