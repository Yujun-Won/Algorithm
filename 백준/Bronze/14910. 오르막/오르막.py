numList = list(map(int, input().split()))
sortedList = sorted(numList)

if numList == sortedList:
  print('Good')
else:
  print('Bad')