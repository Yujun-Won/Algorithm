for _ in range(int(input())):
  N = int(input())
  weights = list(map(int, input().split()))

  sum = 0
  for weight in weights:
    sum += weight

  if sum > 0:
    print("Right")
  elif sum < 0:
    print("Left")
  else:
    print("Equilibrium")