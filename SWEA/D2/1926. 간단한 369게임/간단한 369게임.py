N = int(input())

for i in range(1, N+1):
    if i >= 10:
        target = ['3', '6', '9']
        count = 0

        number = list(str(i))
        for num in number:
            if num in target:
                count += 1   

        if count >= 1:
            print('-' * count, end=' ')
        else:
            print(''.join(number), end=' ')

    else:
        if i % 3 == 0:
            print('-', end=' ')
        else:
            print(i, end=' ')
print()