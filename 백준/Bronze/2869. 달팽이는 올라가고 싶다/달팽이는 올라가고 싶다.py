import sys

A, B, V = map(int, sys.stdin.readline().split())

cnt = (V - B) / (A - B)

if int(cnt) == cnt:
    print(int(cnt))
else:
    print(int(cnt) + 1)
