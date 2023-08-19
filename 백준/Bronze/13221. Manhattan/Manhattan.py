x, y = map(int, input().split())
N = int(input())

numList = []
distList = []
for _ in range(N):
  x1, y1 = map(int, input().split())
  distance = abs(x1-x) + abs(y1-y)
  numList.append((x1, y1))
  distList.append(distance)

x, y = numList[distList.index(min(distList))]
print(x, y)