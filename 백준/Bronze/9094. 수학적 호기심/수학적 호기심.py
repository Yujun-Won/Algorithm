import sys
from itertools import combinations

T = int(sys.stdin.readline())
for _ in range(T):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    cnt = 0
    for i in combinations(range(1, n), 2):
        a, b = i
        temp = (a**2 + b**2 + m) / (a * b)
        if temp.is_integer():
            cnt += 1
    print(cnt)