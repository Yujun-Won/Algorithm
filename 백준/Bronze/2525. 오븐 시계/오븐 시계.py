A, B = map(int, input().split())
C = int(input())

minute = B + C
hour = minute // 60  # minute을 60으로 나눈 몫을 hour로 담음

if hour >= 1:
  A += hour
  minute -= hour*60
  if A >= 24:
    A -= 24
  print(A, minute)
else:                # hour의 변화가 없는 경우
  print(A, minute)