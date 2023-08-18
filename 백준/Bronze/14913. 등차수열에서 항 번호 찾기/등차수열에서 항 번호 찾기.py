a, d, k = map(int, input().split())

dn = k - a + d

if dn % d == 0 and dn // d >= 1:
  print(dn // d)
else:
  print('X')