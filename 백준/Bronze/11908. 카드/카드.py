N = int(input())
numList = list(map(int, input().split()))

numList.sort()
sum = 0
for i in range(N-1):
  sum += numList[i]

print(sum)