from itertools import combinations

def isPrime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def solution(nums):
    cases = list(combinations(nums, 3))
    
    numbers = [a + b + c for a, b, c in cases]
    
    result = [number for number in numbers if isPrime(number) is True]

    return len(result)