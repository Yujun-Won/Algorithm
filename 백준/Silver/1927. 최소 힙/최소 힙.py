import sys
import heapq

heap = []

for _ in range(int(sys.stdin.readline())):
    num = int(sys.stdin.readline())

    if num == 0:
        if len(heap) > 0:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, num)
