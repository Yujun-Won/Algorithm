T = int(input())

for case in range(T):
    result = 0
    numbers = list(map(int, input().split()))
    
    for num in numbers:
        if num % 2 != 0:
            result += num

    print(f"#{case + 1} {result}")
