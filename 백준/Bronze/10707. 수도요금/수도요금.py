A = int(input())      # X사의 1리터당 요금
B = int(input())      # Y사의 기본요금
C = int(input())      # Y사의 요금이 기본요금이 되는 사용량의 상한
D = int(input())      # Y사의 1리터 당 추가요금
P = int(input())      # JOI군의 집에서 사용하는 한 달간 수도의 양

useX = A * P
if P <= C:            # 기본요금 미만 사용
  useY = B
elif P > C:
  useY = B + (P-C) * D

if useX < useY:
  print(useX)
else:
  print(useY)
  