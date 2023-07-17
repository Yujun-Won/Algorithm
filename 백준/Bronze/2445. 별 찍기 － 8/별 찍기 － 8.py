num = int(input())

for i in range(1, 2*num):
    if i < num:
        print("*"*i + " "*(2*num - 2*i) + "*"*i)
    elif i == num:
        print("*"*(2*num))
    elif i > num:
        print("*"*(2*num - i) + " "*(2*i -2*num) + "*"*(2*num - i))