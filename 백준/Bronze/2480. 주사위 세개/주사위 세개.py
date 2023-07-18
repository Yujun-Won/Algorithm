a, b, c = map(int, input().split())

if a == b and b == c:
  result = 10000 + a * 1000
elif a == b and b != c and c != a:
  result = 1000 + a * 100
elif a != b and b != c and c == a:
  result = 1000 + a * 100
elif a != b and b == c and c != a:
  result = 1000 + b * 100
else:
  temp = [a, b, c]
  result = max(temp) * 100

print(result)