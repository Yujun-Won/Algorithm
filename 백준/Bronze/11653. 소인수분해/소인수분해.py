import sys

N = int(sys.stdin.readline())
d = 2

while N >= d:
  if N % d == 0:
    print(d)
    N /= d
  else:
      d += 1