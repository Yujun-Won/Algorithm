N = int(input())
score = list(map(int, input().split()))

M = max(score)
n_score = []
for i in score:
  n_score.append(i/M*100)

sum = 0
for i in n_score:
  sum += i
print(round(sum/len(n_score), 2))