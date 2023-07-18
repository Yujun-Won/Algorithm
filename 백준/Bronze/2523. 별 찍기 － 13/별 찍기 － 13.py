N = int(input())

for i in range(1, 2*N):
  if i <= N:
    print(i*'*')
  elif i > N:
    print((2*N-i)*'*')