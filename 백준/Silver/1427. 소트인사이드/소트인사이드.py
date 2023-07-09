N = input()

numList = [i for i in N]
numList.sort(reverse=True)

answer = ''
for i in numList:
  answer += i

print(int(answer))