import sys
sys.stdin = open('input.txt')

def fn(param, value):
    global result
    count = 0
    for line in lines:
        count += line // param
    if count >= value:
        return True
    return False

def binary_search(lo,hi,value):
    while lo +1 < hi:
        mid = (lo + hi) // 2
        if fn(mid, value):
          lo = mid
        else:
          hi = mid
    if(fn(hi, value)):
        return hi
    return lo

K, N = map(int, sys.stdin.readline().split())

lines = [int(sys.stdin.readline().strip()) for _ in range(K)]
result = 0

result = binary_search(0, max(lines), N)

print(result)

