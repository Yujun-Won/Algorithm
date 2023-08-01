import sys

univW = [int(sys.stdin.readline().rstrip()) for _ in range(10)]
univK = [int(sys.stdin.readline().rstrip()) for _ in range(10)]

print(sum(sorted(univW, reverse=True)[:3]), sum(sorted(univK, reverse=True)[:3]))
