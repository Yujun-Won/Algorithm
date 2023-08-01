import sys

scoreDict = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0,
             'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0}

creditSum, totalSum = 0, 0           # 학점 합계, 종합 합계

for _ in range(20):
    _, credits, score = sys.stdin.readline().rstrip().split()

    if score == 'P':
        continue

    totalSum += float(credits)
    creditSum += float(credits) * scoreDict[score]

print(round(creditSum / totalSum, 6))
