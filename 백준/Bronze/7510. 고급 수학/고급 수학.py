n = int(input())

for i in range(n):
    num = sorted(list(map(int, input().split())))
    if num[2] == ((num[0]**2 + num[1]**2) ** 0.5):
        result = 'yes'
    else:
        result = 'no'
    print("Scenario #{}:".format(i+1))
    print(result)
    print()