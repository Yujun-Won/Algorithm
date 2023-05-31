def solution(n):
    result = [i for i in range(1, n) if n % i == 1]
    return result[0]