T = int(input())          # 테스트 케이스의 개수

for i in range(T):
  A, B = map(int, input().split())
  print(f"Case #{i+1}: {A} + {B} = {A+B}")