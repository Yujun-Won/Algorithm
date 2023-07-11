import sys

N = int(sys.stdin.readline())
As = set(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
Ms = list(map(int, sys.stdin.readline().split()))

for M in Ms:
    if M in As:
        print(1)
    else:
        print(0)