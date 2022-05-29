import sys
import heapq

n = int(sys.stdin.readline())
heap = []
for i in range(n):
    num = int(sys.stdin.readline())
    if num:
        heapq.heappush(heap, (-num, num))
    else:
        if len(heap):
            print(heapq.heappop(heap)[1])
        else:
            print(0)
        