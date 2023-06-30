N = int(input())
calls = list(map(int, input().split()))

yPrice, mPrice = 0, 0

for call in calls:
  yPrice += (call // 30) * 10 + 10
  mPrice += (call // 60) * 15 + 15

if yPrice == mPrice:
  print(f"Y M {yPrice}")
elif yPrice > mPrice:
  print(f"M {mPrice}")
else:
  print(f"Y {yPrice}")