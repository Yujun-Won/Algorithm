N, k = map(int, input().split())

scoreList = list(map(int, input().split()))
scoreList.sort(reverse=True)

print(scoreList[k-1])