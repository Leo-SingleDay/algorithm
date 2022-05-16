import sys
sys.stdin = open('input.txt')

n, m = map(int, sys.stdin.readline().split())
n_arr = set()
for i in range(n):
    n_arr.add(sys.stdin.readline().strip())

cnt = 0
result = []
for _ in range(m):
    person = sys.stdin.readline().strip()
    if person in n_arr:
        cnt += 1
        result.append(person)

print(cnt)
result.sort()
for p in result:
    print(p)
