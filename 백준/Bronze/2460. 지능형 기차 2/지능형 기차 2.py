inList = []
for n in range(10):
    i, o = map(int, input().split())
    if n == 0:
        inList.append(i)
        inList.append(o)
    else:
        inList.append(inList[2*n-1]-i)
        inList.append(inList[2*n]+o)

print(max(inList))