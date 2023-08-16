from itertools import combinations

N, K = map(int, input().split())

numList = list(range(N))
combination = list(combinations(numList, K))

print(len(combination))