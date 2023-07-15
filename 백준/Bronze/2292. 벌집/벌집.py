num = int(input())

roomNum = 1
cnt = 1
while num > roomNum:
  roomNum += 6 * cnt
  cnt += 1
print(cnt)