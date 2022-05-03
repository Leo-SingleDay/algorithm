import sys
sys.stdin = open('input.txt')

def binary_search(start, end, target):
    while start <= end:
        mid = (start+end)//2
        count = 0
        for line in lines:
            count += line//mid
        if count >= target:
            start = mid+1
        else:
            end = mid-1
    return end

K, N = map(int, sys.stdin.readline().split())
lines = [int(sys.stdin.readline().strip()) for _ in range(K)]

result = binary_search(0, max(lines), N)

print(result)

