titleDict = dict()
for _ in range(int(input())):
    book = input()
    if book in titleDict:
        titleDict[book] += 1
    else:
        titleDict[book] = 1

m = max(titleDict.values())
tempList = []
for k, v in titleDict.items():
    if v == m:
        tempList.append(k)

tempList.sort()
print(tempList[0])