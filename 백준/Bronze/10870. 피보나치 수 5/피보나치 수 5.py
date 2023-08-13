def fib(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fib(n-1) + fib(n-2)

fibList = [fib(i) for i in range(21)]

n = int(input())
print(fibList[n])