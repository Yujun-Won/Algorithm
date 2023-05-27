T = int(input())

for i in range(1, T+1):
    numbers = list(map(int, input().split()))

    result = []
    for number in numbers:
        if number < 40:
            result.append(40)
        else:
            result.append(number)

    result = int(sum(result) / len(numbers))

    print(f"#{i} {result}")