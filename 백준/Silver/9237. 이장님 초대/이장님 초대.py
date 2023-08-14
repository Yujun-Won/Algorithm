import sys

N = int(sys.stdin.readline().rstrip())
trees = list(map(int, sys.stdin.readline().rstrip().split()))

trees = sorted(trees, reverse=True)

growingDays = [trees[i] + i + 1 for i in range(len(trees))]

print(max(growingDays) + 1)
