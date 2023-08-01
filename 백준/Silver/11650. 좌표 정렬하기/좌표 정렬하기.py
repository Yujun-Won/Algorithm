import sys

n = int(sys.stdin.readline().rstrip())

points = []
for i in range(n):
  x, y = map(int, sys.stdin.readline().rstrip().split())
  points.append((x, y))
points.sort()

for i in range(n):
  x, y = points[i]
  print("{} {}".format(x, y))