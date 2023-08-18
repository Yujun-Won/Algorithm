numList = list(map(int, input().split()))

result = [i for i in numList if i > 0]
print(len(result))