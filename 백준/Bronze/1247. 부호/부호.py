import sys

for _ in range(3):
  N = int(sys.stdin.readline().rstrip())
  numList = []
  for _ in range(N):
    numList.append(int(sys.stdin.readline().rstrip()))
  S = sum(numList)

  if S > 0:
    print('+')
  elif S < 0:
    print('-')
  elif S == 0:
    print('0')  