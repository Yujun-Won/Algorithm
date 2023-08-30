for _ in range(int(input())):
    number = int(input())

    location = [idx for idx, digit in enumerate(bin(number)[2:][::-1]) if digit == '1']

    for i in location:
        print(i, end=' ')
    print()
