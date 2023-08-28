def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


for _ in range(int(input())):
    n, *arr = map(int, input().split())
    arr.sort()

    result = 0

    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            result += gcd(arr[i], arr[j])

    print(result)
