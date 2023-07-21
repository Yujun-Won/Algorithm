c = int(input())              # 테스트 케이스의 개수

for _ in range(c):
  nums = list(map(int, input().split()))
  n = nums[0]                 # 학생의 수 n
  avg = sum(nums[1:]) / n
  
  cnt = 0
  for i in nums[1:]:
    if i > avg:               # avg보다 높은 점수를 count
      cnt += 1
  overAvg = cnt / n * 100
  print('{:.3f}%'.format(round(overAvg, 3)))