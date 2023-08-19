N = int(input())
S = input()

score, bonus, total = 0, 0, 0
for i in S:
  score += 1
  if i == 'O':
    total += score
    total += bonus
    bonus += 1
  else:
    bonus = 0
print(total)