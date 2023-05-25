T = int(input())

for i in range(1, T+1):
    N = int(input())
    people = list(map(int, input().split()))

    avg = sum(people) / N

    cnt = 0
    for person in people:
        if person <= avg:
            cnt += 1

    print(f"#{i} {cnt}")