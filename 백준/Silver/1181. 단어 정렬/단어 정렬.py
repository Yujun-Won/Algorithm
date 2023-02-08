import sys

N = int(sys.stdin.readline())
strList = [sys.stdin.readline().rstrip() for _ in range(N)]

# set의 특징을 이용하여 중복을 제거, 다시 리스트로 변환
temp = set(strList)
strList = list(temp)

# 알파벳 순서대로 정렬하고, 길이 순서로 정렬
strList.sort()
strList.sort(key=len)

for i in strList:
  print(i)