T = int(input())

for i in range(1, T+1):
    moeum = ['a', 'e', 'i', 'o', 'u']

    test_case = list(input())

    result = [digit for digit in test_case if digit not in moeum]
    result = ''.join(result)

    print(f"#{i} {result}")