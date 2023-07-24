import math

num = [int(input()) for _ in range(5)]

lang = math.ceil(num[1] / num[3])
arith = math.ceil(num[2] / num[4])

if lang > arith:
    print(num[0] - lang)
else:
    print(num[0] - arith)