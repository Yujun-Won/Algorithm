def gcd(n, m):
    for i in range(min(n, m), 0, -1):
        if n % i == 0 and m % i == 0:
            return i


for _ in range(int(input())):
    n, *arr = map(int, input().split())
    arr.sort()

    result = 0

    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            result += gcd(arr[i], arr[j])

    print(result)
