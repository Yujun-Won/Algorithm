T = int(input())

for i in range(1, T+1):
    A, B = map(int, input().split())

    if A > 9 or B > 9:
        result = -1
    else:
        result = A * B

    print(f"#{i} {result}")