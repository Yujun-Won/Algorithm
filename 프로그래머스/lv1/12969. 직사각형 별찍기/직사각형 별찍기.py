a, b = map(int, input().strip().split())

for i in range(1, b+1):
    for j in range(a):
        print('*', end='')
    print()