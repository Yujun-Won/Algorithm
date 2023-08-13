import sys

N = int(sys.stdin.readline())
stack = []

for _ in range(N):
  statement = sys.stdin.readline().rstrip()
  if statement[0:4] == 'push':    # push
    val = statement[5:]
    stack.append(int(val))
  elif statement == 'top':        # top
    if len(stack) == 0:
      print(-1)
    else:
      print(stack[len(stack)-1])
  elif statement == 'size':       # size
    print(len(stack))
  elif statement == 'empty':      # empty
    if len(stack) == 0:
      print(1)
    else:
      print(0)
  elif statement == 'pop':        # pop
    if len(stack) == 0:
      print(-1)
    else:
      print(stack.pop())