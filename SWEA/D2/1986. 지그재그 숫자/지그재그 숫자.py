T = int(input())

for i in range(T):
    N = int(input())
    numbers = [i for i in range(1, N+1)]

    result = 0
    for number in numbers:
        if number % 2 != 0:
            result += number
        else:
            result -= number
    
    print(f"#{i+1} {result}")