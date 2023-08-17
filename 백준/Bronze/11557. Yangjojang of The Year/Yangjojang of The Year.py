T = int(input())

for _ in range(T):
  school = {}
  N = int(input()) 
  for i in range(N):
    a, b = input().split()
    school[a] = int(b)
  n_school = dict(zip(school.values(), school.keys()))
  print(n_school[max(n_school)])