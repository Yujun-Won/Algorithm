N = int(input())
cnt = 0

for _ in range(N):
  temp = input()
  day = int(temp[2:])
  if day <= 90:
    cnt += 1

print(cnt)