# 7개의 자연수
# 홀수인 자연수를 모두 골라 그 합을 구하기
# 홀수들 중 최솟값을 찾기

numbers = [int(input()) for _ in range(7)]

odds = [number for number in numbers if number % 2 != 0]

if len(odds) != 0:
    odds.sort()

    print(sum(odds))
    print(odds[0])
else:
    print(-1)
