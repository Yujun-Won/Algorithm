T = int(input())

for i in range(1, T+1):
    N, K = map(int, input().split())
    assignments = list(map(int, input().split()))

    students = list(range(1, N+1))

    for assignment in assignments:
        students.remove(assignment)

    print(f"#{i}", end=' ')
    for num in students:
        print(num, end=' ')
    print()