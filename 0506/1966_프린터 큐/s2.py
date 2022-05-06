import sys
from collections import deque
sys.stdin = open('input.txt')

for _ in range(int(sys.stdin.readline())):
    n, m = map(int, sys.stdin.readline().strip().split())
    queue = deque()

    temp = list(map(int, sys.stdin.readline().strip().split()))
    for i in range(n):
        queue.append(temp[i])

    count = 0
    while True:
        if m == 0:
            if max(queue) == queue[0]:
                count += 1
                break
            else:
                queue.append(queue.popleft())
                m += (len(queue)-1)
        elif max(queue) == queue[0]:
            queue.popleft()
            count += 1
            m -= 1
        else:
            queue.append(queue.popleft())
            m -= 1
    print(count)
