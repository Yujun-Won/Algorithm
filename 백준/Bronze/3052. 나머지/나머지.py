num = []
for _ in range(10):
  num.append(int(input()))

result = []
for i in num:
  result.append(i % 42)

cnt = 0
for i in range(42):
  a = result.count(i)
  if a > 1:
    a = 1
  cnt += a

print(cnt)