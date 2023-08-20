string = input()
cntA, cntB = 0, 0

for i in string:
    if i == 'A':
        cntA += 1
    elif i == 'B':
        cntB += 1
print("{} : {}".format(cntA, cntB))