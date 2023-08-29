import heapq
import sys

q1 = []      # 음수 넣을 힙
q2 = []      # 양수 넣을 힙

for i in range(int(sys.stdin.readline())):
    num = int(sys.stdin.readline().rstrip())

    # 1. 입력이 양수 또는 음수: heappush
    if num < 0:
        heapq.heappush(q1, -num)      # 음수 입력
    elif num > 0:
        heapq.heappush(q2, num)       # 양수 입력
    # 2. 입력이 0: heappop
    else:
        if not q1:              # q1이 비어 있을 때
            if not q2:          # q2가 비어 있다면
                print(0)
            else:               # q2가 비어있지 않다면
                print(heapq.heappop(q2))
        elif not q2:            # q1이 비어 있지 않을 때 q2가 비어 있다면
            print(-heapq.heappop(q1))
        else:                   # q1, q2 모두 비어 있지 않을 때
            temp1 = -heapq.heappop(q1)
            temp2 = heapq.heappop(q2)

            # q1과 q2를 하나씩 heappop하고, 절대값이 작은 값을 출력
            if abs(temp1) > abs(temp2):
                print(temp2)
                heapq.heappush(q1, -temp1)
            else:
                print(temp1)
                heapq.heappush(q2, temp2)
