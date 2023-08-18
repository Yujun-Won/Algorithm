from itertools import combinations

friends = list(map(int, input().split()))

sumList = []
for team in combinations(friends, 2):
    sumList.append(sum(team))
sumList.sort()

print(sumList[3]-sumList[2])