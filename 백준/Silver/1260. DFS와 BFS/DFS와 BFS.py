import sys
from collections import defaultdict, deque


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for neighbor in sorted(graph[v]):       # 정점 번호가 작은 것을 먼저 방문
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)


def bfs(graph, start):
    visited = {node: False for node in graph}
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for neighbor in sorted(graph[v]):   # 정점 번호가 작은 것을 먼저 방문
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True


N, M, V = map(int, sys.stdin.readline().rstrip().split())

graph = defaultdict(list)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

visited = {node: False for node in range(1, N+1)}
dfs(graph, V, visited)
print()
bfs(graph, V)
print()
