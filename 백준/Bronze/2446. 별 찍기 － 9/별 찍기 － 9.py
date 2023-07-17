num = int(input())

for i in range(1, 2*num):
    if i <= num:
        print(" "*(i-1) + "*"*(2*num - 2*i + 1))
    else:
        print(" "*(2*num - i - 1) + "*"*(2*i - (2*num - 1)))