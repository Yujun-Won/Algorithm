from collections import deque

N = int(input())

deq = deque([i for i in range(1, N+1)])

while len(deq) > 1:
    # 1. 맨 위 카드 버리기
    deq.popleft()

    # 2. 그 다음 맨 위 카드를 맨 아래로
    deq.rotate(-1)

print(deq[0])
