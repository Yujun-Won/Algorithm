import sys
from collections import Counter

px = []
py = []

for _ in range(3):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    px.append(x)
    py.append(y)

x_counts = Counter(px)
y_counts = Counter(py)

x = [i for i, count in x_counts.items() if count == 1][0]
y = [i for i, count in y_counts.items() if count == 1][0]

print(x, y)
