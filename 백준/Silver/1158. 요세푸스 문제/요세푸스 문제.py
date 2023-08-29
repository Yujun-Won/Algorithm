from collections import deque

N, K = map(int, input().split())
result = []

circle = deque([i for i in range(1, N+1)])

while len(circle) > 0:
    circle.rotate(-1 * (K-1))
    result.append(circle.popleft())

print('<', ', '.join(map(str, result)), '>', sep='')
