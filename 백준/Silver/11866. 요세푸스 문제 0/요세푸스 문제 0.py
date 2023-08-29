from collections import deque

N, K = map(int, input().split())
result = []

que = deque([i for i in range(1, N+1)])

while len(que) > 0:
    que.rotate(-1 * (K-1))
    result.append(que.popleft())

print('<', ', '.join(map(str, result)), '>', sep='')
