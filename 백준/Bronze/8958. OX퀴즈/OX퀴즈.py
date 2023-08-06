T = int(input())

for _ in range(T):
    ox = input()
    sum = 0
    score = 0
    for i in ox:
        if i == 'O':    # O 동안 score 축적
            score += 1
        else:
            score = 0
        sum += score
    print(sum)