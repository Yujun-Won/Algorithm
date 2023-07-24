secList = [int(input()) for _ in range(4)]

total = sum(secList)
print(total // 60)
print(total % 60)