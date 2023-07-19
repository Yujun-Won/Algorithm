inputList = []
for _ in range(5):
  inputList.append(list(map(int, input().split())))

outputList = []
for i in range(5):
  outputList.append(sum(inputList[i]))

print(outputList.index(max(outputList))+1, max(outputList))