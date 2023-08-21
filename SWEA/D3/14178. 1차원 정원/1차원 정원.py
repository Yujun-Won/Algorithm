T = int(input())

for i in range(T):
    N, D = map(int, input().split())
    length = 2 * D + 1

    result = N // length
    N -= length * result

    if N != 0:
        result += 1

    print(f"#{i+1} {result}")
