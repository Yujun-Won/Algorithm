v = int(input())
vote = input()

cntA, cntB = 0, 0

for i in vote:
  if i == 'A':
    cntA += 1
  elif i == 'B':
    cntB += 1

if cntA > cntB:
  print('A')
elif cntA < cntB:
  print('B')
else:
  print('Tie')