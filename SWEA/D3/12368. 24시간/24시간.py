T = int(input())

for i in range(1, T+1):
    A, B = map(int, input().split())

    time = A + B

    if time >= 24:
        time -= 24

    print(f"#{i} {time}")