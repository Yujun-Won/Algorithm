num = int(input())

for i in range(1, num+1):
    print(" " * (i-1) + "*" * ((2*num)-(2*i-1)))