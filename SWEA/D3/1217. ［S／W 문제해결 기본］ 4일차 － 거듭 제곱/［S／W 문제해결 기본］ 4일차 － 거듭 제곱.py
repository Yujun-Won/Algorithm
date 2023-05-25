for i in range(10):
    testcase = int(input())
    N, M = map(int, input().split())

    print(f"#{i+1} {N ** M}")