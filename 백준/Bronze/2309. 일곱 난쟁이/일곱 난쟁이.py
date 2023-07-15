from itertools import combinations

height = [int(input()) for _ in range(9)]

for combi in combinations(height, 7):
  if sum(combi) == 100:
    for i in sorted(combi):
      print(i)
    break