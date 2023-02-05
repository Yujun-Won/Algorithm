n = int(input())

num = n                     # n을 쪼개기 위한 변수
cnt = 0

while True:
  a, b = num//10, num%10    # num의 십의 자리, 일의 자리
  c = (a+b) % 10            # 새로운 일의 자리
  num = b*10 + c            # 새로운 숫자

  cnt += 1
  if num == n:
    break

print(cnt)