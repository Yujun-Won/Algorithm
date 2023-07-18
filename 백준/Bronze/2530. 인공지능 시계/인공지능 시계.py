a, b, c = map(int, input().split())
d = int(input())

hour, min, sec = d//3600, (d%3600)//60, (d%3600)%60

a += hour
b += min
c += sec

if c >= 60:
  plusMin = c//60
  c -= 60 * plusMin
  b += plusMin

if b >= 60:
  plusHour = b//60
  b -= 60 * plusHour
  a += plusHour

if a >= 24:
  plusDay = a//24
  a -= 24 * plusDay

print(a, b, c)