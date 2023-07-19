A, B = map(int, input().split())

a, b, c = A//100, (A//10) % 10, A % 10
x, y, z = B//100, (B//10) % 10, B % 10

A_new = 100*c + 10*b + a
B_new = 100*z + 10*y + x

if A_new > B_new:
  print(A_new)
elif A_new < B_new:
  print(B_new)