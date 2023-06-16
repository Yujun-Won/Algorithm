n = int(input())
p = list(map(int, input().split()))

total_time, time = 0, 0
time_list = []

p.sort()
for i in p:
  time += i
  time_list.append(time)

total_time = sum(time_list)
print(total_time)