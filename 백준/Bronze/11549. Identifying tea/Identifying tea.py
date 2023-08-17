tea = int(input())
answers = list(map(int, input().split()))

score = 0
for answer in answers:
    if answer == tea:
        score += 1
print(score)