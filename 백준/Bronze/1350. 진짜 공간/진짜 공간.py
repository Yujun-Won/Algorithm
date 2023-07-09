import math

n = int(input())
files = list(map(int, input().split()))
cluster = int(input())

cnt = []
for file in files:
    cnt.append(math.ceil(file / cluster))

print(cluster * sum(cnt))    