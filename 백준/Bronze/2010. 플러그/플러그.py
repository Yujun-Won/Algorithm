import sys

plugs = [int(sys.stdin.readline().rstrip()) for _ in range(int(sys.stdin.readline().rstrip()))]
print(sum(plugs) - len(plugs) + 1)
